import random
import pprint

def pp(p: int) -> None:
	pprint.PrettyPrinter(indent=4).pprint(p)

class MarkovChain:
	def __init__(self, s: list, k: int):
		self.samples = s
		self.k = k
		self.chain = self.create()
		self.state = tuple(self.samples[:self.k])
		self.words = "".join(self.samples).split(" ")

	def create(self) -> dict:
		n = {}

		self.samples = list(filter(lambda x: x != '', self.samples))

		for i in range(len(self.samples)):
			ng = tuple(self.samples[i:i+self.k])
			nxt = self.samples[(i+self.k) % len(self.samples)]

			if ng not in n:
				n[ng] = {"freq": 0, "states": {}}
			
			n[ng]["freq"] += 1
			
			if nxt not in n[ng]["states"]:
				n[ng]["states"][nxt] = {"freq": 0}			

			n[ng]["states"][nxt]["freq"] += 1

		# convert into percentages
		for i in n:
			for j in n[i]["states"]:
				n[i]["states"][j] = n[i]["states"][j]["freq"] / n[i]["freq"]
			# restructure
			n[i].pop("freq")
			n[i] = n[i]["states"]

		return n

	def next(self) -> str:
		if self.state not in self.chain:
			# bodge
			self.state = random.choices(list(self.chain.keys()))[0]

		return random.choices(
			list(self.chain[self.state].keys()),
			weights=self.chain[self.state].values())[0]

	def gen_words(self, m: int) -> list:
		w = []
		for i in range(m):
			n = self.next()
			self.state = self.state[1:] + (n,)
			w.append(n)

		return list(filter(lambda x: x in self.words, "".join(w).split(" ")))

	def gen_sentence(self, n: int) -> str:
		return " ".join(c.gen_words(n))

import sys
f=open(sys.argv[1],"r")
r=f.read().replace("\n"," ")
c=MarkovChain(r,int(sys.argv[2]))
print(c.gen_sentence(10000))

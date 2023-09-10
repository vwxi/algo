class Node:
	def __init__(self, v, state=0, parent=0):
		self.val = v
		self.parent = parent
		self.children = {}
		self.end = False
		self.state = state
		self.suffix = 0
		self.output = 0
		self.word = False

	def __repr__(self):
		s="Node(state={}, val=\'{}\', parent={}, children=[{}], suffix={}, end={}, word={})"
		return s.format(
			self.state,
			self.val,
			self.parent,
			"" if self.end else ", ".join([self.children[i].__repr__() for i in self.children]),
			self.suffix,
			self.end,
			self.word
		)
	
class AhoCorasick:
	def __init__(self, kw, text):
		self.keywords = kw
		self.head = Node("")
		self.counter = 1
		self.text = text
		self.next = []
		
		for i in self.keywords:
			self.insert(i)

		self.construct()

	def construct(self):
		Q=[]
		v=set()

		Q.append(self.head.state)
		while len(Q) != 0:
			n = self.ssearch(Q[0]); Q = Q[1:]
			for c in n.children.values():
				if c.state not in v:
					v.add(c.state)
					Q.append(c.state)
					
					if c.parent == 0:
						c.suffix = 0
					else:
						e = self.ssearch(n.suffix)
						while True:
							if c.val in e.children:
								c.suffix = e.children[c.val].state
								break
							elif e.state == 0:
								c.suffix = 0
								break

							e = self.ssearch(e.suffix)

					u = self.ssearch(c.suffix)
					if u.word: c.output = u.state
					else: c.output = u.output

	def _ssearch(self, state, ptr):
		if ptr == None: return None
		if ptr.state == state: return ptr
		for i in ptr.children.values():
			f = self._ssearch(state, i)
			if f != None: return f
		
	def ssearch(self, state):
		return self._ssearch(state, self.head)

	def insert(self, key):
		ptr = self.head

		for i in key:	
			if i not in ptr.children:
				ptr.end = False
				ptr.children[i] = Node(i, self.counter, ptr.state)
				self.counter += 1
			ptr = ptr.children[i]
		ptr.end = True
		ptr.word = True

	def pt(self,ptr):
		p=ptr
		a=""
		while p!=self.head:
			a+=p.val
			p=self.ssearch(p.parent)
		return a[::-1]

	def search(self):
		ptr = self.head
		found = []

		for i in range(len(self.text)):
			while self.text[i] not in ptr.children and ptr != self.head:
				ptr = self.ssearch(ptr.suffix)

			if self.text[i] in ptr.children:
				ptr = ptr.children[self.text[i]]
			else:
				ptr = self.head

			if ptr.word:
				s = self.pt(ptr)
				found.append([s, i-len(s)+1])

		return found

a=AhoCorasick(["he","she","his","hers"], "ushers")
print(a.search())

class Graph:
	def __init__(self):
		self.graph = {}
	
	def add_vertex(self, v):
		if v in self.graph:
			raise ValueError("vertex in graph already exists")
		self.graph[v] = {}

	def add_edge(self, p1, p2, d):
		if p1 not in self.graph or p2 not in self.graph:
			raise ValueError("one of the vertices doesn't exist")

		if p2 in self.graph[p1] or p1 in self.graph[p2]:
			raise ValueError("edge already exists between vertices")

		self.graph[p1][p2] = d
		self.graph[p2][p1] = d

class Digraph(Graph):
	def __init__(self):
		super().__init__()

	# single direction only
	def add_edge(self, p1, p2, d):
		if p1 not in self.graph or p2 not in self.graph:
			raise ValueError("one of the vertices doesn't exist")

		self.graph[p1][p2] = d

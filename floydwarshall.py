from graph import Digraph
from math import *

def fw(g: Digraph, a, b):
	m = [[inf for _ in g.graph] for _ in g.graph]
	l = [i for i in g.graph]
	p = [[inf for _ in g.graph] for _ in g.graph]

	# create adjancency matrix from graph
	# and setup path
	for i in range(len(l)):
		for j in range(len(l)):
			if l[i] == l[j]:
				m[i][i] = 0
			elif l[j] not in g.graph[l[i]]:
				m[i][j] = inf
			else:
				m[i][j] = g.graph[l[i]][l[j]]

			p[i][j] = j

	# iteratevely find the shortest path lengths
	# improve on each k iteration
	for k in range(len(g.graph)):
		for i in range(len(g.graph)):
			for j in range(len(g.graph)):
				t = m[i][k]+m[k][j]
				if t < m[i][j]:
					m[i][j] = t	
					p[i][j] = p[i][k]

	# reverse traversal to obtain real path
	w = []
	while a != b:
		w.append(a)
		a = p[a][b]

	w.append(b)
	return w	

# test cases
#g = Digraph()
#g.add_vertex("A")
#g.add_vertex("B")
#g.add_vertex("C")
#g.add_vertex("D")
#g.add_vertex("E")
#g.add_vertex("F")
#g.add_vertex("G")
#g.add_edge("A", "B", 5)
#g.add_edge("A", "C", 3)
#g.add_edge("A", "D", 6)
#g.add_edge("B", "C", 6)
#g.add_edge("B", "E", 4)
#g.add_edge("C", "E", 6)
#g.add_edge("C", "D", 7)
#g.add_edge("D", "F", 2)
#g.add_edge("D", "E", 2)
#g.add_edge("E", "G", 3)
#g.add_edge("E", "F", 4)
#g.add_edge("F", "G", 5)
#print(fw(g, 0, 6))

#g = Digraph()
#g.add_vertex(1)
#g.add_vertex(2)
#g.add_vertex(3)
#g.add_vertex(4)
#g.add_edge(1, 3, -2)
#g.add_edge(3, 4, 2)
#g.add_edge(4, 2, -1)
#g.add_edge(2, 3, 3)
#g.add_edge(2, 1, 4)
#print(fw(g, 0, 3))

#g = Digraph()
#g.add_vertex(1)
#g.add_vertex(2)
#g.add_vertex(3)
#g.add_vertex(4)
#g.add_vertex(5)
#g.add_edge(2, 1, 3)
#g.add_edge(1, 3, 6)
#g.add_edge(3, 4, 2)
#g.add_edge(4, 3, 1)
#g.add_edge(1, 3, 3)
#g.add_edge(4, 2, 1)
#g.add_edge(5, 4, 2)
#g.add_edge(5, 2, 4)
#print(fw(g, 1, 4))

g = Digraph()
[g.add_vertex(i) for i in range(4)]
g.add_edge(0, 2, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 1, 2)
g.add_edge(1, 2, 6)
g.add_edge(1, 0, 7)
print(fw(g, 1, 3))

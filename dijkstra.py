from graph import Graph
import json
import math

def dijkstra(g: Graph, s, e):
	if s not in g.graph or e not in g.graph:
		raise ValueError("start/end doesn't exist in graph")
#	print(json.dumps(g.graph, indent=2)) #format graph
	cur = s
	
	uv = {i: math.inf for i in g.graph}
	vs = {i: False for i in g.graph}
	pv = {i: None for i in g.graph}
	uv[cur] = 0
	
	while vs[e] == False:
		nn = [i for i in g.graph[cur] if vs[i] == False]
		for n in nn:
			td = uv[cur] + g.graph[cur][n]
			if td < uv[n]:
				uv[n] = td
				pv[n] = cur

		k = sorted(list(filter(lambda x: vs[x] == False, vs)), key=uv.get)
		cur = k[0]
		vs[cur] = True


	# reverse traversal to find result
	k = pv[e]
	w = []
	w.append(e)
	while k != None:
		w.append(k)
		k = pv[k]

	return w[::-1]

### test cases

# example graph from wikipedia
#g = Graph()
#g.add_vertex("1")
#g.add_vertex("2")
#g.add_vertex("3")
#g.add_vertex("4")
#g.add_vertex("5")
#g.add_vertex("6")
#g.add_edge("1", "2", 7)
#g.add_edge("1", "6", 14)
#g.add_edge("1", "3", 9)
#g.add_edge("2", "3", 10)
#g.add_edge("6", "3", 2)
#g.add_edge("6", "5", 9)
#g.add_edge("5", "4", 6)
#g.add_edge("2", "4", 15)
#g.add_edge("3", "4", 11)
#print(dijkstra(g, "1", "5"))

# A D E G
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 3)
g.add_edge("A", "D", 6)
g.add_edge("B", "C", 6)
g.add_edge("B", "E", 4)
g.add_edge("C", "E", 6)
g.add_edge("C", "D", 7)
g.add_edge("D", "F", 2)
g.add_edge("D", "E", 2)
g.add_edge("E", "G", 3)
g.add_edge("E", "F", 4)
g.add_edge("F", "G", 5)
print(dijkstra(g, "A", "G"))

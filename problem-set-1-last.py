# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
def get_all_nodes(graph):
	nodes = []
	for edge in graph:
		for node in edge:
			if (not node in nodes):
				nodes.append(node)
	return nodes

def pick_edge(start, unvisited_edges):
	for i, edge in enumerate(unvisited_edges):
			if (edge[0] == start):
				next_start = edge[1]
				return [i, edge, next_start]
			elif (edge[1] == start):
				next_start = edge[0]
				return [i, edge, next_start] 

def find_eulerian_tour(graph):
	tour = []
	unvisited_edges = [n for n in graph]
	nodes = get_all_nodes(graph)
	start = nodes[0]
	while len(unvisited_edges) > 0:
		next_edge = pick_edge(start, unvisited_edges)
		tour.append(next_edge[1])
		unvisited_edges.pop(next_edge[0])
		start = next_edge[2]
	return tour

print find_eulerian_tour([(1,2),(2,3),(1,3)])

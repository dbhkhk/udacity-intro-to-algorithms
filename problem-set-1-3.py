# solution 1, simple solution
def edge(node1, node2):
	return (node1, node2) if node1 < node2 else (node2, node1)

def create_tour(nodes):
	tour = []
	l = len(nodes)
	for i in range(l):
		t = edge(nodes[i], nodes[(i+1) % l])
		tour.append(t)
	return tour

print create_tour([1,5,2,4,3])

# solution 2
from random import randint

# pop a random node out of a nodes list and return it
def poprandom(nodes): #
	x_i = randint(0, len(nodes) - 1) # get a random index
	return nodes.pop(x_i)

# return a random node from a node list
def pickrandom(nodes):
	x_i = randint(0, len(nodes) - 1)
	return nodes[x_i]

# try to connect node x with each node in nodes list
# once a new edge is found, add it to tour and
# pop out the node from nodes list, and return it
# if no new edge can be created, return None
def check_nodes(x, nodes, tour):
	for i, n in enumerate(nodes):
		t = edge(x, n)
		if t not in tour:
			tour.append(t)
			nodes.pop(i)
			return n
	return None

def create_tour_random(nodes):
	connected = []
	degree = {}
	unconnected = [n for n in nodes]
	tour = []
	# first, pick two random nodes for an edge
	x = poprandom(unconnected)
	y = poprandom(unconnected)
	connected.append(x)
	connected.append(y)
	tour.append(edge(x,y))
	degree[x] = 1
	degree[y] = 1
	# then, pick a random node from the connected and 
	# pop a random node from unconnected to create an edge
	while len(unconnected) > 0:
		x = pickrandom(connected)
		y = poprandom(unconnected)
		connected.append(y)
		tour.append(edge(x,y))
		degree[x] += 1
		degree[y] = 1
	# now make sure each node has an even degree
	odd_nodes = [k for k, v in degree.items() if v % 2 == 1]
	even_nodes = [k for k, v in degree.items() if v % 2 == 0]
	# there will always be an even number of odd_nodes
	# so we connect pairs of unconnected odd_nodes
	while len(odd_nodes) > 0:
		x = poprandom(odd_nodes)
		cn = check_nodes(x, odd_nodes, tour)
		if cn is not None:
			even_nodes.append(x)
			even_nodes.append(cn)
		else:
			# if we get here, the node is already connected to
			# all odd_nodes, so we need to find an even node to connect
			cn = check_nodes(x, even_nodes, tour)
			# cn cannot be None, and needs to be added to odd_nodes
			odd_nodes.append(cn)
			# x is now an even node
			even_nodes.append(x)
	return tour
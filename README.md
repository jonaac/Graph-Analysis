# GraphAnalysis

The goal is to disconnect a graph of North American cities by using edge betweenness. The graph consists of 312 North American cities. The edges represent cities' nearest neighbours by distance. It is derived from the USCA312 dataset (local copy), which includes the entire distance matrix between cities. The edges are undirected.

Each city has x & y coordinates representing its geographic location (derived from the latitude and longitude). These are used to plot the graph.

The file city-graph.txt serializes the graph. Each non-indented line describes a city, giving its

- name,
- province (that is, state or province),
- x & y geographic coordinates of the city,
- the number of following indented lines that list (some of) its neighbouring cities
- (the “edges” it participates in), and
- the number of neighbouring cities (“edges”) for the city in total.

The indented lines following a city line gives
- the name & province of the neighbouring city, and
- the distance in miles (sorry!) to that neighbouring city. (You will not be using this information in this project. We only care whether there is an edge between two cities or not.)

Find the “original” USCA312 dataset at GitHub. Thanks to John Burkardt presently at Virginia Tech, previously at Florida State University, who further curated the USCA312 dataset (FSU copy).

## Algorithm

I want to remove edges based on edge betweenness with respect to the graph to break the graph into two connnected components; thus, to identify “communities” of North American cities.

I did this by the following algorithm.

- I repeatedly remove the edge with the largest betweenness score until the graph is disconnected.
- After each edge removal, I recompute the remaining edges' betweenness scores — that is, with respect to the ”new” graph that resulted from the previous edge removal — since the edges' betweenness scores may now have changed.
- Once the graph has become disconnected, I add back as many edges to the graph that you had deleted as possible that still leaves the graph disconnected. (this is simply adding back each deleted edge that is between nodes in one or the other connected component, but that is not a “bridge” edges between the two components)

When I ran this on the city graph, my program removed 20 edges, then returned 9, leaving a eleven-edge cut of the graph. Note that a plot of the “cut” graph might not readily show a clear two regions with no lines between them; that also depends on how the graph is plotted with node position information. In this case, however, the separation is visually apparent.

### Module networkx

Module networkx is a comprehensive Python library for handling graphs and performing graph analytics. I used it's Graph() class for handling the graph. It contains some rather useful methods, including

- is_connected(G), and
- edge_betweenness_centrality(G).

### Module matplotlib

I used matplotlib to plot your graph. I plotted the graph for the full city graph as follows.

```python
import matplotlib.pyplot as plot
import networkx as nx
    ⋮ 
G = nx.Graph()
positions = {} # a position map of the nodes (cities)
    ⋮ 
plot the city graph
plot.figure(figsize=(8,8))
nx.draw(G,
        positions,
        node_size   = [4 for v in G],
        with_labels = False)

#plot.savefig('city-plot.png')
plot.show()
```


```python
#Hash Table Collision

class Item:

	def __init__(self,key,value):
		self.key = key
		self.value = value

class HashTable:

	def __init__(self):
		self.size = 1000
		self.data = [[]] * self.size

	def hash(key):
		return int(key)%(self.size)

	def put(self,key,val):
		item = Item(key,val)
		index = hash(key)
		found = False
		if self.data[index] != []:
			i = 0
			while i < len(self.data[index]) and not found:
				if self.data[index][i].key == item.key or self.data[index][i] == None:
					self.data[index][i] = item
					found = True
				i += 1
			if not found:
				self.data[index].append(item)
		else:
			self.data[index].append(item)

	def get(self,key):
		index = hash(key)
		if len(self.data[index]) == 0:
			raise NameError('EmptyHash')
		else:
			for item in self.data[index]:
				if item.key == key:
					return item.value
			raise NameError('NotInHash')

	def delelte(self,key):
		index = hash(key)
		if len(self.data[index]) == 0:
			raise NameError('EmptyHash')
		else:
			i = 0
			while i < len(self.data[index]):
				if self.data[index][i].key == item.key:
					self.data[index][i] = None
					return
				i += 1
			raise NameError('NotInHash')

	def len(self):
		return self.size

	def exists(self,key):
		index = hash(key)
		if len(self.data[index]) == 0:
			raise NameError('EmptyHash')
		else:
			for item in self.data[index]:
				if item.key == key:
					return True
			return False
```

import matplotlib.pyplot as plot
import networkx as nx

G = nx.Graph()
positions = {}      # a position map of the nodes (cities)
nodes = {}          #dictionary that holds all the nodes and their betweeness scores
maxBetweeness = 0.0 #holds the value of the edge with the highest Betweeness score
removedEdges = []   #Keeps a list of the edges that were removed to later be used to add them back (as long as the graph stays disconnected)


with open("city-graph.txt", "r") as inFile:
    lines = inFile.readlines()
    currentLine = 0
    while currentLine < len(lines):
        line = lines[currentLine]
        details = [x.strip() for x in line.split(',')]  #seperate the lines into different to extract the name, province, x&y coordinates, and number of indented lines (edges it participates in)
        name = details[0] + ", " + details[1]           #Extract the name, province to be used as the node name
        xPos = float(details[2])                        #x-coordinate value
        yPos = float(details[3])                        #y-coordinate value
        numNeighbours = int(details[4])                 #number of indented lines (edges node participates in)

        # add the node
        G.add_node(name, pos=(xPos, yPos))
        
        #iterates through the indented lines adding the appropriate edges
        for i in range(numNeighbours):
            currentLine += 1
            neighbourDetails = [x.strip() for x in lines[currentLine].split(',')]
            neighbourName = neighbourDetails[0] + ", " + neighbourDetails[1]
            neighbourWeight = float(neighbourDetails[2])
            
            #add the edge
            G.add_edge(name, neighbourName, weight=neighbourWeight)
        currentLine += 1

#populate nodes dictionary with the node and betweeness information
nodes = nx.edge_betweenness_centrality(G)

#As long as the graph is connected keep removing edges and store them into removeEdges for future reference
while nx.is_connected(G):
    edgeToRemove = None
    maxBetweeness = 0.0
    for key, value in nodes.items():
        if value > maxBetweeness:
            maxBetweeness = value
            edgeToRemove = key
    if edgeToRemove is not None:
        removedEdges.append(edgeToRemove)
        edge1, edge2 = edgeToRemove
        print ("attempting to remove edge: %s -> %s" % (edge1, edge2))   
        G.remove_edge(edge1, edge2)
        print ("removed edge: %s -> %s" % (edge1, edge2))
        nodes = nx.edge_betweenness_centrality(G)

#count=0
for x in removedEdges:
    edge1, edge2 = x
    G.add_edge(edge1, edge2)  
    print ("added edge: %s -> %s" % (edge1, edge2))
    #count = count + 1
    if nx.is_connected(G):
        G.remove_edge(edge1,edge2)
        print ("removed edge: %s -> %s" % (edge1, edge2))
        #print("LENGHT OF REMOVED EDGE:", len(removedEdges))
        #count = count -1    
#print (count)

plot.figure(figsize=(8, 8))
nx.draw(G,
        nx.get_node_attributes(G, 'pos'),
        node_size=[4 for v in G],
        with_labels=False)

plot.savefig('city-plot.png')
plot.show()

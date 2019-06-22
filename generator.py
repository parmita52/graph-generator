#########################
######## Imports ########
#########################

import matplotlib.pyplot as plt
import numpy as np
import json
import random
import networkx as nx

#########################
####### Constants #######
#########################

WEIGHT_MIN_DEFAULT = 0
WEIGHT_MAX_DEFAULT = 10
NUM_NODES_DEFAULT = 10
NUM_EDGES_DEFAULT = 10

#########################
#### Data Structures ####
#########################
class UserInput:
    def __init__(self, numOfNodes, numOfEdges, isDirected, isMultigraph, hasSelfLoops, isWeighted, weightMin=WEIGHT_MIN_DEFAULT, weightMax=WEIGHT_MAX_DEFAULT, weightIsFloat=False):
        self.numOfNodes = numOfNodes
        self.numOfEdges = numOfEdges
        self.isDirected = isDirected
        self.isMultigraph = isMultigraph
        # self.numOfConnectedComponents = numOfConnectedComponents
        # self.isTree = isTree
        self.hasSelfLoops = hasSelfLoops
        self.isWeighted = isWeighted
        if self.isWeighted:
            self.weightMin = weightMin
            self.weightMax = weightMax
            self.weightIsFloat = weightIsFloat

    @classmethod
    def fromJSON(cls, data):
        numOfNodes = int(data.get("numOfNodes", NUM_NODES_DEFAULT))
        numOfEdges = int(data.get("numOfEdges", NUM_EDGES_DEFAULT))
        isDirected = bool(data.get("isDirected", False))
        isMultigraph = bool(data.get("isMultigraph", False))
        # numOfConnectedComponents = bool(data.get("numOfConnectedComponents", False))
        # isTree = bool(data.get("isTree", False))
        hasSelfLoops = bool(data.get("hasSelfLoops", False))
        isWeighted = bool(data.get("isWeighted", False))
        if isWeighted:
            weightMin = int(data.get('weightMin', WEIGHT_MIN_DEFAULT))
            weightMax = int(data.get('weightMax', WEIGHT_MAX_DEFAULT))
            weightIsFloat = bool(data.get('isFloat', False))
            return cls(numOfNodes, numOfEdges, isDirected, isMultigraph, hasSelfLoops, isWeighted, weightMin, weightMax, weightIsFloat)
        else:
            return cls(numOfNodes, numOfEdges, isDirected, isMultigraph, hasSelfLoops, isWeighted)

    @classmethod
    def fromPath(cls, pathname):
        with open(pathname) as json_file:
            data = json.loads(json_file.read())
        return cls.fromJSON(data)
        
    @classmethod
    def fromRequest(cls, request):
        data = request.args.to_dict()
        return cls.fromJSON(data)
        
#########################
### Helper Functions ####
#########################

def add_weights(G, userInput):
    for (source, target) in G.edges:
        G[source][target]['weight'] = random.uniform(userInput.weightMin, userInput.weightMax) if userInput.weightIsFloat else random.randint(userInput.weightMin, userInput.weightMax)
    return G

# Remove self loops from edgeList
def remove_self_loops(edgeList):
    return list(filter(lambda x : x[0] != x[1], edgeList))

# Remove directed edges from edgeList
def remove_directed_edges(edgeList):
    return list(filter(lambda x : x[0] >= x[1], edgeList))

def draw_graph(G):
    # print(G.edges)
    for (a,b) in G.edges:
        print(a, b, G[a][b]['weight'])
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw(G, with_labels=True)
    pos = nx.drawing.layout.spring_layout(G)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

#########################
## Generator Functions ##
#########################

def generate_graph(userInput):
    D = userInput.isDirected
    M = userInput.isMultigraph
    n = userInput.numOfNodes
    allEdges = [(i, j) for i in range(n) for j in range(n)]

    if (not D) and (not M):
        G = generate_Graph(userInput, allEdges)
    elif (not D) and (M):
        G = generate_MultiGraph(userInput, allEdges)
    elif (D) and (not M):
        G = generate_DiGraph(userInput, allEdges)
    elif (D) and (M):
        G = generate_MultiDiGraph(userInput, allEdges)
    
    if userInput.isWeighted:
        G = add_weights(G, userInput)
     
    # draw_graph(G)
    return G

def generate_Graph(userInput, allEdges):
    if not(userInput.hasSelfLoops): 
        allEdges = remove_self_loops(allEdges)
    allEdges = remove_directed_edges(allEdges)
    finalEdges = random.sample(allEdges, userInput.numOfEdges)
    G = nx.from_edgelist(finalEdges, create_using=nx.Graph)
    return G

def generate_MultiGraph(userInput, allEdges):    
    if not(userInput.hasSelfLoops): 
        allEdges = remove_self_loops(allEdges)
    allEdges = list(filter(lambda x : x[0] >= x[1], allEdges))
    finalEdges = []
    for _ in range(userInput.numOfEdges):
        finalEdges.append(random.choice(allEdges))
    G = nx.from_edgelist(finalEdges, create_using=nx.MultiGraph)
    return G

def generate_DiGraph(userInput, allEdges):
    if not(userInput.hasSelfLoops): 
        allEdges = remove_self_loops(allEdges)
    finalEdges = random.sample(allEdges, userInput.numOfEdges)
    G = nx.from_edgelist(finalEdges, create_using=nx.DiGraph)
    return G

def generate_MultiDiGraph(userInput, allEdges):
    if not(userInput.hasSelfLoops): 
        allEdges = remove_self_loops(allEdges)
    allEdges = list(filter(lambda x : x[0] >= x[1], allEdges))
    finalEdges = []
    for _ in range(userInput.numOfEdges):
        finalEdges.append(random.choice(allEdges))
    G = nx.from_edgelist(finalEdges, create_using=nx.MultiDiGraph)
    return G

#########################
##### Main Function #####
#########################

def main():
    test_sample()

def test_sample():
    # path = "./samples/sample1.json"
    # path = "./samples/sample2.json"
    path = "./samples/sample3.json"
    userInput = UserInput.fromJSON(path)
    generate_graph(userInput)

if __name__ == "__main__":
    main()

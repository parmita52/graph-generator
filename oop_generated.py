#########################
######## Imports ########
#########################

import matplotlib.pyplot as plt
import numpy as np
import json
import random
import networkx as nx

#########################
### Helper Functions ####
#########################
class UserInput:
    def __init__(self, pathname):
        with open(pathname) as json_file:
            data = json.loads(json_file.read())
        self.numOfNodes = data["numOfNodes"]
        self.numOfEdges = data["numOfEdges"]
        self.averageDegree = data["averageDegree"]
        self.isDirected = data["isDirected"]
        self.numOfConnectedComponents = data["numOfConnectedComponents"]
        self.isMultigraph = data["isMultigraph"]
        self.isTree = data["isTree"]
        self.hasSelfLoops = data["hasSelfLoops"]
        self.weight = data["weight"]

def decide_case(userInput):
    D = userInput.isDirected
    M = userInput.isMultigraph
    S = userInput.hasSelfLoops
    if (not D) and (not M) and (not S):
    elif (not D) and (not M) and (S):
    elif (not D) and (M) and (not S):
    elif (not D) and (M) and (S):
    elif (D) and (not M) and (not S):
    elif (D) and (not M) and (S):
    elif (D) and (M) and (not S):
    elif (D) and (M) and (S):
    else:
        print("yikes")

def generate_edge_list(userInput):
    nodes = list(range(userInput.numOfNodes))
    edge_list = [(0,1), (0,2), (1,2), (1,3), (2,3), (1,4), (3,4)]
    return edge_list
    # TODO decide to either create a list of edges and make Graph
    # or loop through and add edges
    # decide on NetworkX graph class early on?
    # ^^ should this just make edge list or return whole graph?

    ### check for numOfEdges vs averageDegree
    ### check for isDirected
    ### check for numOfConnectedComponents
    ### check for isMultigraph
    ### check for isTree
    ### check for hasSelfLoops
    ### check for weight


def test_sample1():
    path = "./samples/sample1.json"
    userInput = UserInput(path)
    G = nx.Graph()
    ### TODO the possible classes are:
    # Graph, DiGraph, MultiGraph, or MultiDiGraph
    G.add_edges_from(generate_edge_list(userInput))
    draw_graph(G)

def draw_graph(G):
    nx.draw(G)
    plt.show()

#########################
##### Main Function #####
#########################

def main():
    test_sample1()

if __name__ == "__main__":
    main()

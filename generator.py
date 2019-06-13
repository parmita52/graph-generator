#########################
######## Imports ########
#########################

import matplotlib.pyplot as plt
import numpy as np
import json
import random

#########################
### Helper Functions ####
#########################

def user_input_json(pathname):
    with open(pathname) as json_file:
        data = json.loads(json_file.read())
    return data

def generate_graph():
    data = user_input_json("./samples/sample1.json")
    n = data['numOfNodes']
    e = data['numOfEdges']
    hasSelfLoops = data['hasSelfLoops']
    isDirected = data['isDirected']
    edgeList = generate_list_of_edges(n, e, hasSelfLoops, isDirected)
    generate_adjacency_matrix(edgeList, n)
    adjacencyList = generate_adjacency_list(edgeList, n)
    adjacencyMatrix = generate_adjacency_matrix(edgeList, n)
    print(adjacencyList)
    print(adjacencyMatrix)

def generate_adjacency_matrix(edgeList, n):
    matrix = np.zeros(shape=(n,n))
    for (a, b) in edgeList:
        matrix[a][b] = 1
    return matrix

def generate_adjacency_list(edgeList, n):
    adjacencyList = dict()
    for vertex in range(n):
        adjacencyList[vertex] = []
    for (i, j) in edgeList:
        adjacencyList[i].append(j)
    return adjacencyList

def generate_all_possible_edges(n, e, hasSelfLoops, isDirected):
    allEdges = [(i, j) for i in range(n) for j in range(n)]
    if not hasSelfLoops:
        allEdges = list(filter(lambda x : x[0] != x[1], allEdges))
    if not isDirected:
        allEdges = list(filter(lambda x : x[0] >= x[1], allEdges))
    return allEdges

def generate_list_of_edges(n, e, hasSelfLoops, isDirected):
    allEdges = generate_all_possible_edges(n, e, hasSelfLoops, isDirected)
    if e > len(allEdges):
        raise Error("too many edges")
    edgeList = random.sample(allEdges, e)
    if not isDirected:
        flatten = lambda l: [item for sublist in l for item in sublist]
        edgeList = flatten(map(lambda x : [(x[0], x[1]), (x[1], x[0])], edgeList))
    return edgeList

def draw_graph():
    pass

#########################
##### Main Function #####
#########################

def main():
    generate_graph()

if __name__ == "__main__":
    main()

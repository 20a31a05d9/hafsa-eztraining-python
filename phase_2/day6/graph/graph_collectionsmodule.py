# import dictionary for graph
from collections import defaultdict

# add edge to graph
graph=defaultdict(list)

def addEdge(graph,u,v):
    graph[u].append(v)

def generate_edges(graph):
    edges=[]
    #for each node in graph
    for node in graph:
        #for each neighbour node of a single node
        for neighbour in graph[node]:
            #if edge exsits then append
            edges.append((node,neighbour))
    return edges

addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

#printing graph 
print(generate_edges(graph))

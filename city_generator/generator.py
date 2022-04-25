import numpy as np
from city_generator.city import city
from multipledispatch import dispatch

@dispatch(list)
def generateCities(inputs):

    np.random.seed(19680801)
    cities = []
    distanceTable = [[0 for i in range(inputs[0])] for j in range(inputs[0])]

    # inputs[0] = the number of nodes, inputs[1] = the lower bound, and inputs[2] = the upper bound.

    for i in range(inputs[0]):
        cityObj = city(i, np.random.randint(inputs[1],inputs[2]), np.random.randint(inputs[1],inputs[2]))
        cities.append(cityObj)

    for i in range(len(cities)):
        for node in cities:
            if i != node.node:
                edge = {"linkedNode": node.node, "x": node.x, "y": node.y, "distance": np.linalg.norm(np.array([cities[i].x, cities[i].y]) - np.array([node.x, node.y]))}
                cities[i].edges.append(edge)

    for i in range(0, len(cities)):
        for j in range(0, len(cities)-1):
            distanceTable[cities[i].node][cities[i].edges[j]['linkedNode']] = cities[i].edges[j]['distance']

    return cities, distanceTable

@dispatch(str)
def generateCities(TSPfile):
    file = open(TSPfile, "r")
    lines = file.readlines()
    formatted_lines = []
    counter_ = 0
    counter = 0
    TSP_dimension = 0
    for line in lines:
        counter_ += 1
        formatted_lines.append(line.rstrip("\n"))
        if line.rstrip("\n") == "NODE_COORD_SECTION":
            counter = counter_ # The first node of the TSP starts on this counter value.
        if line.rstrip("\n").startswith("DIMENSION"):
            TSP_dimension = int(line.rstrip("\n").split()[2])

    EOF = counter + TSP_dimension

    TSP_nodes = []
    while counter < EOF:
        node = []
        for value in formatted_lines[counter].split(" "):
            node.append(float(value))
        TSP_nodes.append(node)
        counter += 1

    cities = []
    distanceTable = [[0 for i in range(TSP_dimension)] for j in range(TSP_dimension)]

    for i in range(TSP_dimension):
        cityObj = city(i, TSP_nodes[i][1], TSP_nodes[i][2])
        cities.append(cityObj)

    for i in range(len(cities)):
        for node in cities:
            if i != node.node:
                edge = {"linkedNode": node.node, "x": node.x, "y": node.y, "distance": np.linalg.norm(np.array([cities[i].x, cities[i].y]) - np.array([node.x, node.y])) }
                cities[i].edges.append(edge)

    for i in range(0, len(cities)):
        for j in range(0, len(cities)-1):
            distanceTable[cities[i].node][cities[i].edges[j]['linkedNode']] = cities[i].edges[j]['distance']

    return cities, distanceTable

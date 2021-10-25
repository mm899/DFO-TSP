import matplotlib.pyplot as plt

def plot(cities, swarm, distanceTable, showAllEdges):
    for city in cities:
        plt.scatter(city.x, city.y, label=f"City: {city.node}", s=20, zorder=5)

    for city in cities:
        for edge in city.edges:
            plt.plot((city.x, edge['x']), (city.y, edge['y']), c='lightgrey')

    if showAllEdges == 1:
        for fly in range(len(swarm)):
            for dimension in range(len(swarm[fly])):
                if dimension != len(swarm[fly]) - 1:
                    x = []
                    y = []
                    currentFly = swarm[fly][dimension]
                    nextFly = swarm[fly][dimension + 1]
                    for city in cities:
                        if city.node == currentFly:
                            x.append(city.x)
                            y.append(city.y)
                            for edge in city.edges:
                                if edge['linkedNode'] == nextFly:
                                    x.append(edge['x'])
                                    y.append(edge['y'])
                    plt.plot(x, y, label=f"Distance/Cost: {distanceTable[currentFly][nextFly]}", linewidth=2.5)
                else:
                    x = []
                    y = []
                    currentFly = swarm[fly][dimension]
                    nextFly = swarm[fly][0]
                    for city in cities:
                        if city.node == currentFly:
                            x.append(city.x)
                            y.append(city.y)
                            for edge in city.edges:
                                if edge['linkedNode'] == nextFly:
                                    x.append(edge['x'])
                                    y.append(edge['y'])
                    plt.plot(x, y, label=f"Distance/Cost: {distanceTable[currentFly][nextFly]}", linewidth=2)

    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', ncol=2)
    plt.tight_layout()
    plt.show()
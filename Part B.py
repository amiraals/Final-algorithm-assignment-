import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Intersections:
    def __init__(self, intersectionID):
        self.intersectionID = intersectionID

class Roads:
    def __init__(self, roadID, sourceIntersect, destIntersect, roadName, length):
        self.roadID = roadID
        self.sourceIntersect = sourceIntersect
        self.destIntersect = destIntersect
        self.roadName = roadName
        self.length = length

class Houses:
    def __init__(self, houseID):
        self.houseID = houseID

class RoadNetworks:
    def __init__(self):
        self.intersections = {}
        self.roads = {}
        self.houses = {}

    def addIntersection(self, intersectionID):
        if intersectionID not in self.intersections:
            self.intersections[intersectionID] = Intersections(intersectionID)

    def addRoad(self, roadID, sourceIntersectID, destIntersectID, roadName, length):
        self.addIntersection(sourceIntersectID)
        self.addIntersection(destIntersectID)
        self.roads[roadID] = Roads(roadID, sourceIntersectID, destIntersectID, roadName, length)

    def addHouse(self, houseID):
        if houseID not in self.houses:
            self.houses[houseID] = Houses(houseID)

    def addPackage(self, houseID, intersectionID):
        self.addHouse(houseID)
        self.addIntersection(intersectionID)
        self.roads[f'package_{houseID}_{intersectionID}'] = Roads(f'package_{houseID}_{intersectionID}', intersectionID, houseID, 'Package Delivery', 0.001)

    def getRoadInfo(self, roadID):
        road = self.roads.get(roadID)
        if road:
            return {
                'Road ID': road.roadID,
                'Source Intersection': road.sourceIntersect,
                'Destination Intersection': road.destIntersect,
                'Road Name': road.roadName,
                'Length': road.length
            }
        else:
            return None

    def getIntersectionInfo(self, intersectionID):
        intersection = self.intersections.get(intersectionID)
        if intersection:
            return {'intersection ID': intersection.intersectionID}
        else:
            return None

    def dijkstra_shortest_path(self, sourceIntersectID, destIntersectID):
        distances = {intersectionID: float('inf') for intersectionID in self.intersections}
        distances[sourceIntersectID] = 0
        visited = set()
        priorityQ = [(0, sourceIntersectID)]

        while priorityQ:
            distU, u = heapq.heappop(priorityQ)
            if u in visited:
                continue
            visited.add(u)
            if u == destIntersectID:
                return distances[destIntersectID]
            for roadID, road in self.roads.items():
                if road.sourceIntersect == u:
                    v = road.destIntersect
                    alt = distU + road.length
                    if alt < distances[v]:
                        distances[v] = alt
                        heapq.heappush(priorityQ, (alt, v))
        return float('inf')

    def shortestDist(self, sourceIntersectID, destIntersectID):
        return self.dijkstra_shortest_path(sourceIntersectID, destIntersectID)

    def distributePackages(self):
        for houseID, house in self.houses.items():
            shortestDist = float('inf')
            closestIntersect = None
            for intersectionID in self.intersections:
                distance = self.shortestDist(intersectionID, houseID)
                if distance < shortestDist:
                    shortestDist = distance
                    closestIntersect = intersectionID
            print(f"The shortest distance from intersection {intersectionID} to house {houseID} is: {distance}")

def plotGraph(roadNetwork):
    G = nx.Graph()
    for intersectionID in roadNetwork.intersections:
        G.add_node(intersectionID, color='green')

    for houseID in roadNetwork.houses:
        G.add_node(houseID, color='red')

    for roadID, road in roadNetwork.roads.items():
        G.add_edge(road.sourceIntersect, road.destIntersect, label=f'Road {roadID}')

    pos = nx.spring_layout(G)
    node_colors = [node[1]['color'] for node in G.nodes(data=True)]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, alpha=0.7)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()


# Test cases
roadNetwork = RoadNetworks()

# Add intersections
roadNetwork.addIntersection(1)
roadNetwork.addIntersection(2)
roadNetwork.addIntersection(3)
roadNetwork.addIntersection(4)

# Add roads
roadNetwork.addRoad(1, 1, 2, 'Road 1', 2)
roadNetwork.addRoad(2, 2, 3, 'Road 2', 3)
roadNetwork.addRoad(3, 3, 4, 'Road 3', 1)
roadNetwork.addRoad(4, 4, 1, 'Road 4', 2)

# Add houses
roadNetwork.addHouse(101)
roadNetwork.addHouse(102)

# Add packages
roadNetwork.addPackage(101, 1)
roadNetwork.addPackage(102, 4)

# Plot the graph
plotGraph(roadNetwork)

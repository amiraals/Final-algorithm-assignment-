import heapq
import matplotlib.pyplot as plt

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

    def shortestDist(self, sourceIntersectID, destIntersectID):
        distances = {}
        for intersectionID in self.intersections:
            distances[intersectionID] = float('inf')
        distances[sourceIntersectID] = 0

        priorityQ = [(0, sourceIntersectID)]
        while priorityQ:
            distU, u = heapq.heappop(priorityQ)
            if distU > distances[u]:
                continue
            for roadID, road in self.roads.items():
                if road.sourceIntersect == u:
                    v = road.destIntersect
                    alt = distU + road.length
                    if alt < distances[v]:
                        distances[v] = alt
                        heapq.heappush(priorityQ, (alt, v))
        return distances[destIntersectID]

    def shortestPaths(self, source, destination):
        distances = {intersectionID: float('inf') for intersectionID in self.intersections}
        distances[source] = 0
        priorityQ = [(0, source)]
        visited = set()

        while priorityQ:
            distU, u = heapq.heappop(priorityQ)
            if u in visited:
                continue
            visited.add(u)

            if u == destination:
                break

            for roadID, road in self.roads.items():
                if road.sourceIntersect == u:
                    v = road.destIntersect
                    alt = distU + road.length
                    if alt < distances[v]:
                        distances[v] = alt
                        heapq.heappush(priorityQ, (alt, v))

        return distances[destination]

    def distributePackages(self):
        for houseID, house in self.houses.items():
            shortestDist = float('inf')
            closestIntersect = None
            for intersectionID in self.intersections:
                distance = self.shortestDist(intersectionID, houseID)
                if distance < shortestDist:
                    shortestDist = distance
                    closestIntersect = intersectionID
            print(f"Package for house {houseID} should be delivered from intersection {closestIntersect}")

def plotGraph(roadNetwork):
    fig, ax = plt.subplots()

    # Plot intersections as squares
    for intersectionID, intersection in roadNetwork.intersections.items():
        ax.scatter(intersectionID, 0, color='green', marker='s', label=f'Intersection {intersectionID}')

    # Plot houses as triangles
    for houseID, house in roadNetwork.houses.items():
        ax.scatter(houseID, 0, color='red', marker='^', label=f'House {houseID}')

    # Plot roads as lines
    for roadID, road in roadNetwork.roads.items():
        sourceIntersect = road.sourceIntersect
        destIntersect = road.destIntersect
        ax.plot([sourceIntersect, destIntersect], [0, 0], color='black', linestyle='-', linewidth=1,
                label=f'Road {roadID}')

    ax.set_xlabel('Node ID')
    ax.set_ylabel('Y')
    ax.set_title('Road Network Graph')
    ax.legend()
    plt.show()
plotGraph(roadNetwork)

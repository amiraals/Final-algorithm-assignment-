import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Intersections:
    """
    This class represents the intersections in a road network
    """
    def __init__(self, intersectionID):
        self.intersectionID = intersectionID

class Roads:
    """
    This class represents roads connecting intersections in a road network
    """
    def __init__(self, roadID, sourceIntersect, destIntersect, roadName, length):
        self.roadID = roadID
        self.sourceIntersect = sourceIntersect
        self.destIntersect = destIntersect
        self.roadName = roadName
        self.length = length

class Houses:
    """
    This class represents the houses in a road network
    """
    def __init__(self, houseID):
        self.houseID = houseID

class RoadNetworks:
    """
    This class represents a road network which manages the intersections, roads, and houses in the road network
    """
    def __init__(self):
        self.intersections = {}
        self.roads = {}
        self.houses = {}
    def addIntersection(self, intersectionID):  # Method to add an intersection to the road network
        if intersectionID not in self.intersections:  # Check if intersectionID is not already in the intersections dictionary
            self.intersections[intersectionID] = Intersections(intersectionID)  # If its not in the dictionary add it to intersections dictionary with an Intersection object

    def addRoad(self, roadID, sourceIntersectID, destIntersectID, roadName, length):  # Method to add a road to the road network
        self.addIntersection(sourceIntersectID)  # Make sure the source intersection is added to the road network
        self.addIntersection(destIntersectID)  # Make sure the destination intersection is added to the road network
        self.roads[roadID] = Roads(roadID, sourceIntersectID, destIntersectID, roadName, length)  # Add the road to the roads dictionary with a Roads object

    def addHouse(self, houseID):  # Method to add a house to the road network
        if houseID not in self.houses:  # Check if houseID is not in the houses dictionary
            self.houses[houseID] = Houses(houseID)  # Add houseID to the houses dictionary with a Houses object

    def addPackage(self, houseID, intersectionID):  # Method to add a package delivery point to the road network
        self.addHouse(houseID)  # Make sure that the house is added to the road network
        self.addIntersection(intersectionID)  # Make sure the intersection is added to the road network
        # Add the package delivery point to the roads dictionary with a Roads object
        self.roads[f'package_{houseID}_{intersectionID}'] = Roads(f'package_{houseID}_{intersectionID}', intersectionID, houseID, 'Package Delivery', 0.001)
        
    def getRoadInfo(self, roadID):  # Method to get information about a road
        road = self.roads.get(roadID)  # Get the road object from the roads dictionary using the roadID
        if road:  # Check if road object exists
            # If the road exists, return a dictionary containing information about the road
            return {  
                'Road ID': road.roadID,
                'Source Intersection': road.sourceIntersect,
                'Destination Intersection': road.destIntersect,
                'Road Name': road.roadName,
                'Length': road.length
            }
        else:
            return None  # If it does not exist, return None

    def getIntersectionInfo(self, intersectionID):  # Method to get information about an intersection
        intersection = self.intersections.get(intersectionID)  # Get the intersection object from the intersections dictionary using the intersectionID
        if intersection:  # Check if the intersection object exists
            return {'intersection ID': intersection.intersectionID}  # If the intersection exists, return a dictionary with information about the intersection
        else:
            return None  # If it does not exist, return None
            
    def dijkstra_shortest_path(self, sourceIntersectID, destIntersectID):  # Dijkstra's algorithm to find shortest distance between intersections
        distances = {intersectionID: float('inf') for intersectionID in self.intersections}  # Initialize distances to infinity
        distances[sourceIntersectID] = 0  # Set distance to source intersection to 0
        visited = set()  # Create a set to keep track of visited intersections
        priorityQ = [(0, sourceIntersectID)]  # Priority queue with source intersection and distance 0

        while priorityQ:
            distU, u = heapq.heappop(priorityQ)  # Pop intersection with smallest distance from priority queue
            if u in visited:  # Skip if intersection visited
                continue
            visited.add(u)  # Mark as visited
            if u == destIntersectID:  # Check if destination intersection is reached
                return distances[destIntersectID]  # Return shortest distance to destination
            for roadID, road in self.roads.items(): 
                if road.sourceIntersect == u:  # Check if road starts at current intersection
                    v = road.destIntersect  # Get destination intersection
                    alt = distU + road.length  # Calculate alternative distance
                    if alt < distances[v]:  # Update distance if shorter
                        distances[v] = alt
                        heapq.heappush(priorityQ, (alt, v))  # Push updated distance to priority queue
        return float('inf')  # Return infinity if destination is unreachable

    def shortestDist(self, sourceIntersectID, destIntersectID): # Method to calculate the shortest distance between two intersections
        return self.dijkstra_shortest_path(sourceIntersectID, destIntersectID)

    def distributePackages(self): # Method to distribute packages to the nearest intersection
        for houseID, house in self.houses.items():
            shortestDist = float('inf')
            closestIntersect = None
            for intersectionID in self.intersections:
                distance = self.shortestDist(intersectionID, houseID)
                if distance < shortestDist:
                    shortestDist = distance
                    closestIntersect = intersectionID
            print(f"The shortest distance from intersection {intersectionID} to house {houseID} is: {distance}")

def plotGraph(roadNetwork): # Plots the road network graph
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

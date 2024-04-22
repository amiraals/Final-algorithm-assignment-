import heapq
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

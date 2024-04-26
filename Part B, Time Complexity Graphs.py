import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = np.array([1, 2, 5, 10, 20])

# Create arrays to store the execution time for each algorithm
search_time_dijkstra = np.zeros_like(n, dtype=float)
search_time_shortestDist = np.zeros_like(n, dtype=float)
search_time_distributePackages = np.zeros_like(n, dtype=float)

# Measure the execution time for each algorithm with varying input sizes
for i, num_intersections in enumerate(n):
    roadNetwork = RoadNetworks()

    # Add intersections
    for j in range(1, num_intersections + 1):
        roadNetwork.addIntersection(j)

    # Add roads
    for j in range(1, num_intersections):
        roadNetwork.addRoad(j, j, j+1, f'Road {j}', 1)
# Measure the execution time
    # Dijkstra's algorithm
    start_time = time.time()
    roadNetwork.dijkstra_shortest_path(1, num_intersections)
    search_time_dijkstra[i] = time.time() - start_time

    # shortestDist method
    start_time = time.time()
    roadNetwork.shortestDist(1, num_intersections)
    search_time_shortestDist[i] = time.time() - start_time

    # distributePackages method
    start_time = time.time()
    roadNetwork.distributePackages()
    search_time_distributePackages[i] = time.time() - start_time

# Plot the graphs
plt.figure(figsize=(10, 15))

# Dijkstra's algorithm
plt.subplot(3, 1, 1)
plt.plot(n, search_time_dijkstra, marker='o', label='Dijkstra\'s Algorithm')
plt.ylabel('Time (s)')
plt.xlabel('Number of Intersections (n)')
plt.title('Time Complexity Analysis: Dijkstra\'s Algorithm')
plt.legend()

# shortestDist method
plt.subplot(3, 1, 2)
plt.plot(n, search_time_shortestDist, marker='o', label='shortestDist Method')
plt.ylabel('Time (s)')
plt.xlabel('Number of Intersections (n)')
plt.title('Time Complexity Analysis: shortestDist Method')
plt.legend()

# distributePackages method
plt.subplot(3, 1, 3)
plt.plot(n, search_time_distributePackages, marker='o', label='distributePackages Method')
plt.ylabel('Time (s)')
plt.xlabel('Number of Intersections (n)')
plt.title('Time Complexity Analysis: distributePackages Method')
plt.legend()

plt.tight_layout()
plt.show()

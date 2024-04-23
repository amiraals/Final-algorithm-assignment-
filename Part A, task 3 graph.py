import matplotlib.pyplot as plt
import numpy as np

# Number of posts (n)
n = np.arange(1, 1001, 10)

# Time complexity for creating max heap (O(n log n))
time_complexity = n * np.log(n)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(n, time_complexity, label='O(n log n)', color='blue')
plt.title('Time Complexity of Creating Max Heap')
plt.xlabel('Number of Posts (n)')
plt.ylabel('Time Complexity')
plt.grid(True)
plt.legend()
plt.show()

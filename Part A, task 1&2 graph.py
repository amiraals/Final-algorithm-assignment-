import matplotlib.pyplot as plt
import numpy as np


# First plot, time complexity of finding a post by datetime

# Array of n values (number of posts)
n = np.array([0, 100, 200, 300, 400, 500])

# Array of corresponding search times (seconds)
search_time = np.array([
    0.000004,
    0.000004,
    0.000004,
    0.00000403,
    0.000004,
    0.00000398,
])

plt.figure(figsize=(10, 5))

plt.subplot(1, 1, 1)
plt.plot(n, search_time, marker='o', linestyle='-', color='b', label='Find Post by Datetime')
plt.xlabel('Number of posts (n)')
plt.ylabel('Time (seconds)')
plt.title('Search Time Complexity for Finding a Post by Datetime')

plt.ylim(0.0000025, 0.0000045)

plt.legend()
plt.tight_layout()
plt.show()




# Second plot, time complexity of finding posts in a specific time range

# Array of n values (number of posts)
n = np.array([0, 100, 200, 300, 400, 500])

# Array of corresponding search times (seconds)
search_time = np.array([
    0.000010,
    0.000102,
    0.000192,
    0.000289,
    0.000342,
    0.000419,
])

plt.figure(figsize=(10, 5))

plt.subplot(1, 1, 1)
plt.plot(n, search_time, marker='o', linestyle='-', color='b', label='Find Post in Specific Time Range')
plt.xlabel('Number of posts (n)')
plt.ylabel('Time (seconds)')
plt.title('Search Time Complexity for Finding a Post in Specific Time Range')

plt.ylim(0.0000010, 0.0008)

plt.legend()
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Define the range of data set sizes
data_set_sizes = list(range(1, 1001))

# Define the constant time complexity (O(1)) for hash table find operation
time_complexity = [1] * len(data_set_sizes)

# Plot the time complexity graph
plt.figure(figsize=(10, 6))
plt.plot(data_set_sizes, time_complexity, label='Hash Table (O(1))', color='blue')

# Add labels and title
plt.title('Time Complexity of Hash Table for Finding a Post by Datetime')
plt.xlabel('Size of Data Set')
plt.ylabel('Time Complexity (O(1))')
plt.legend()
plt.grid(True)

# Show the graph
plt.show()

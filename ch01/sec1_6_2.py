import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.arange(0, 6, 0.1) # Generate values from 0 to 6 with a step of 0.1
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle = "--", label='cos') # Plot with dashed line
plt.xlabel("x") # x-axis label
plt.ylabel("y") # y-axis label
plt.title("sin & cos") # Title
plt.legend()
plt.show()
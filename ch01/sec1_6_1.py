import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.arange(0, 6, 0.1) # Generate values from 0 to 6 with a step of 0.1
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
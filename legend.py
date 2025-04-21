# %%
import matplotlib.pyplot as plt
import numpy as np

# Sample data for two lines
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the figure and axes
plt.figure(figsize=(8, 6))
plt.plot(x, y1, color='blue', linestyle='-', label='Sine Wave')  # Add label for the first line
plt.plot(x, y2, color='red', linestyle='--', label='Cosine Wave') # Add label for the second line

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Waves')

# Add the legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
# %%

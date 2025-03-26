

import matplotlib.pyplot as plt

# Simple graph
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title("Simple Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["y = x^2"])
plt.show()

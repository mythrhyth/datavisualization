import matplotlib.pyplot as plt 
x_values = list(range(5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = x_values, cmap = plt.cm.Blues, edgecolors= 'none', s = 40)

plt.show()
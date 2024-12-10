
import matplotlib.pyplot as plt
from random_walk import Randomwalk


rw = Randomwalk(5000)
rw.fill_walk()

plt.plot(rw.x_values, rw.y_values)

#Set the size of the plotting window. 
plt.figure(figsize = (10, 6))

plt.scatter(0, 0, c = 'green', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], s = 100, c = 'red')

plt.show()

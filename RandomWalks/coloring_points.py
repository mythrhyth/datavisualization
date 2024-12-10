import matplotlib.pyplot as plt 
from RandomWalks.random_walk import Randomwalk
rw = Randomwalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s= 15)


#Emphasize the first and last points
plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s= 100)

plt.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s= 1)

#Remove the axes. 


plt.show()

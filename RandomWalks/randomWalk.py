import matplotlib.pyplot as plt 
from RandomWalks.random_walk import Randomwalk
rw = Randomwalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s = 15)
plt.show()
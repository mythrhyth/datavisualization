import matplotlib.pyplot as plt
from RandomWalks.random_walk import Randomwalk
while True:
    rw = Randomwalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s = 15)
    plt.show()
    
    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break
import matplotlib.pyplot as plt
from RandomWalks.random_walk import Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s = 15 )
    
    #Set the size of the plotting window. 
    plt.figure(figsize = (10, 6))
    
    plt.show()
    keep_running = input("do you want more randomwalk? (y/n)")
    if(keep_running == 'n'):
        break
    
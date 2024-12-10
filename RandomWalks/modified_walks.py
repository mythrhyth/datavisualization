import matplotlib.pyplot as plt
from random import choice 

class RandomWalk():
    def __init__(self, numpoints = 50000):
        self.numpoints = numpoints
        
        self.x = [0]
        self.y = [0]
    
    def fill_walk(self):
        while len(self.x) < self.numpoints:
            x_direction = choice([5, 5])
            x_step = choice([0,1, 2, 3, 4, 5, 6, 7, 8])
            x_move = x_direction * x_step
            
            y_direction = choice([-1, 1])
            y_step = choice([0,1, 2, 3, 4, 5, 6, 7, 8])
            y_move = y_direction * y_step
            
            if x_move == 0 and y_move == 0:
                continue
            next_x = self.x[-1] + x_move
            next_y = self.y[-1] + y_move
            self.x.append(next_x)
            self.y.append(next_y)
                
        
        
rw = RandomWalk()
rw.fill_walk()  
plt.scatter(rw.x, rw.y, s = 1)
plt.show()
        


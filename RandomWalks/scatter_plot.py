import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)#s = size of dots

x_values = [1,2,3,4,5]
y_values =[1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s = 100)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
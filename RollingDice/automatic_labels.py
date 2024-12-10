from die import Die 
import pygal 

die1 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll()
    results.append(result)
    
frequencies = []
max_value = die1.num_sides
for value in range(max_value +1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
hist = pygal.Bar()
hist.title = "D6"
hist.x_labels = range(1 , die1.num_sides + 1)
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'
hist.add('D6', frequencies)

hist.render_to_file('dice_six.svg')
    
    

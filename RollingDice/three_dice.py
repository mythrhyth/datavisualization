from die import Die 
import pygal

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll() + die_3.roll()
    results.append(result)
    
frequencies = []
max_value = die_1.num_sides +die_2.num_sides + die_3.num_sides
for value in range(max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
hist = pygal.Bar()
hist.title = "the rolling of 3 dice"
hist.x_values = range(3, max_value + 1)

hist.x_title = "Result"
hist.y_title = "Frequency"
hist.add('D6+D6+D6', frequencies
)
    
hist.render_to_file('3 dice visual.svg')
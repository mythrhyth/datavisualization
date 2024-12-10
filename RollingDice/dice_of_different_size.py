from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
    
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(max_result +1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
hist = pygal.Bar()
hist.title = "Result of rolling D6 and D10 dice 1000 times."
hist.x_labels = []
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('D6 and D10 visual.svg')
from die import Die
import pygal 

die_1 = Die()
die_2 = Die()

results = []
for rollnum in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_value = die_1.num_sides * die_2.num_sides
  
for value in range(max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
hist = pygal.Bar()
hist.title = "Frequency of multiplication of Dices"
hist.x_title = 'Result'
hist.y_title = 'Frequency'
hist.x_label = range(1, max_value + 1)

hist.add('D6*D6', frequencies)
hist.render_to_file('multiplication.svg')
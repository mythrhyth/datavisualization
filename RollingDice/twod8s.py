from die import Die
import pygal

dice_1 = Die(8)
dice_2 = Die(8)

results = []

for i in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)


frequencies = []
max_value = dice_1.num_sides + dice_2.num_sides
for value in range(max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
hist = pygal.Bar()
hist.title = "Rolling of two D8 die"

hist.x_label = range(2, max_value +1 )
hist.x_title = 'Result'

hist.y_title = 'Frequency'

hist.add('D8 + D8', frequencies)
hist.render_to_file('D8+D8visual.svg')
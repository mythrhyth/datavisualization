from matplotlib import pyplot as plt
from datetime import datetime
import csv
 
filename = 'C:\\DataVisualization\\DownloadingData\\annual-rainfall-by-station-in-mm.csv'

rainfall_2017 = []
stations = []


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
 
    
    for row in reader:
        stations.append(row[0])
        
        rainfall_2017.append(row[5])
    
    stations = stations[:30]
    rainfall_2017 = rainfall_2017[:30]
    print(stations)
    print(rainfall_2017)
        
fig = plt.figure(dpi = 128, figsize = (10, 8))
plt.plot(stations, rainfall_2017, c = 'purple', marker = 'o', linestyle = '-')
plt.title('Rainfalls, 2017', fontsize = 18)
plt.tight_layout()

plt.xlabel('Station', fontsize = 12)
plt.ylabel('Rainfall', fontsize = 12)

plt.xticks(rotation=45, ha='center')

plt.tick_params(axis = 'both', which = 'major', labelsize = 5)

plt.show()

plt.figure(figsize = (10, 8))
plt.title('Rainfall, 2017 (Bar Chart)', fontsize = 18)
plt.bar(stations, rainfall_2017, color = 'blue')
plt.xlabel('Station', fontsize = 12)
plt.ylabel('Rainfall (mm)', fontsize = 12)
plt.xticks(rotation = 90, fontsize = 10)
plt.tight_layout()
plt.show()
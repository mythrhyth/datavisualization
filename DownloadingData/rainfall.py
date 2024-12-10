from matplotlib import pyplot as plt
import csv

filename = 'C:\\DataVisualization\\DownloadingData\\annual-rainfall-by-station-in-mm.csv'

rainfall_2017 = []
stations = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    for row in reader:
        stations.append(row[0])  
        rainfall_2017.append(row[5])   


stations = stations[:30]
rainfall_2017 = rainfall_2017[:30]


print(stations)
print(rainfall_2017)


fig, ax = plt.subplots(1, 2, figsize=(16, 8))  # (1, 2) means 1 row and 2 columns


ax[0].bar(stations, rainfall_2017, color='purple')
ax[0].set_title('Rainfalls, 2017 (Bar Chart)', fontsize=16)
ax[0].set_xlabel('Station', fontsize=10)
ax[0].set_ylabel('Rainfall (mm)', fontsize=10)
ax[0].tick_params(axis='x', rotation=90, labelsize=10)  


ax[1].plot(stations, rainfall_2017, color='blue', marker='o', linestyle='-', linewidth=2)
ax[1].set_title('Rainfalls, 2017 (Line Plot)', fontsize=16)
ax[1].set_xlabel('Station', fontsize=10)
ax[1].set_ylabel('Rainfall (mm)', fontsize=10)
ax[1].tick_params(axis='x', rotation=90, labelsize=8)  


plt.tight_layout()


plt.show()

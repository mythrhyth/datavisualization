import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename1 = 'C:\\DataVisualization\\DownloadingData\\sitka_weather_2014.csv'
filename2 = 'C:\\DataVisualization\\DownloadingData\\death_valley_2014.csv'

sitka_dates = []
sitka_high = []
death_dates = []
death_high = []

with open(filename1) as f1, open(filename2) as f2:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    
    header_row1 = next(reader1)  
    header_row2 = next(reader2)  

    try:
        
        for row in reader1:
            if len(row) < 2:  
                print(f"Skipping incomplete row in Sitka data: {row}")
                continue  

            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')  
                sitka = int(row[1])  
                sitka_high.append(sitka)
                sitka_dates.append(date)
            except ValueError:
                print(f"Skipping invalid row in Sitka data (ValueError): {row}")
        
        
        for row in reader2:
            if len(row) < 2:  
                print(f"Skipping incomplete row in Death Valley data: {row}")
                continue  # Skip incomplete rows

            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')  # Date parsing
                death = int(row[1])  # Temperature parsing
                death_high.append(death)
                death_dates.append(date)
            except ValueError:
                print(f"Skipping invalid row in Death Valley data (ValueError): {row}")

    except ValueError:
        print('Error in data format or conversion.')


fig, ax = plt.subplots(figsize=(10, 6))


ax.plot(sitka_dates, sitka_high, label='Sitka High', color='red')
ax.plot(death_dates, death_high, label='Death Valley High', color='orange')


ax.set_title("Daily High Temperatures - 2014", fontsize=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Temperature (°F)', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)


fig.autofmt_xdate()


ax.legend()


plt.show()

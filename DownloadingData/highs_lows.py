import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'C:\\DataVisualization\\DownloadingData\\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
    highs, dates, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%M-%d')
            
            
            high = int(row[1])
            
            
            low = int(row[3])
            
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)
    print(highs)
    
    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red', alpha = 0.5)
    plt.plot(dates, lows, c = "blue", alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
    plt.title('Daily High And Low Temperatures, July 2014', fontsize = 24)
    fig.autofmt_xdate()
    plt.xlabel('', fontsize = 16)
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize =16)
    plt.show()
    
    first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
    print(first_date)
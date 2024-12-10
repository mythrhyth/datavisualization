import csv
from datetime import datetime

filename = 'C:\\DataVisualization\\DownloadingData\\san_francisco_weather_2014.csv'
with open(filename, encoding = 'utf-8-sig') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    
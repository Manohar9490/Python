# with open("c:/Users/manoh/OneDrive/Documents/Python Scripts/weather_data/weather_data.csv") as weather:
#   weather_content = weather.readlines()
#   print(weather_content)


# import csv

# with open("c:/Users/manoh/OneDrive/Documents/Python Scripts/weather_data/weather_data.csv") as weather:
#   data = csv.reader(weather)
#   temp =[]
#   for i in data:
#     if i[1] !="temp":
#       temp.append((i[1]))
# #   print(temp)
# working with csv file

import pandas;

data = pandas.read_csv("c:/Users/manoh/OneDrive/Documents/Python Scripts/weather_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240928.csv")


# Get data from csv file

# with open ("learning/reading-csv/weather_data.csv") as file:
#     data = file.readlines()

# print(data)

# import csv

# Basic csv reader

# with open("learning/reading-csv/weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)

# Use csv reader to get temperatures from csv file

# with open("learning/reading-csv/weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
# print(temp)

import pandas

# Basic pandas

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# temp = data["temp"]
# print(temp)

# Pandas to dictionary

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# Pandas to list

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# temp_list = data["temp"].to_list()

# print(temp_list)

# Calculate average in pandas

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# average = data["temp"].mean()
# print(average)

# Get the max value in pandas

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# maximum = data["temp"].max()
# print(maximum)

# Get data from columns

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# conditions = data["condition"]
# print(conditions)

# Get data from columns alternative

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# conditions = data.condition
# print(conditions)

# Get data from rows

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# monday = data[data.day == "Monday"]
# print(monday)

# Get row where temperature was at the maximum

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# maximum_day = data[data.temp == data.temp.max()]
# print(maximum_day)

# Get data from individual row

# data = pandas.read_csv("learning/reading-csv/weather_data.csv")
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print((monday_temp * 1.8) + 32)

# Create dataframe from scratch

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }

# dataframe = pandas.DataFrame(data_dict)

# print(dataframe)

# Convert dataframe to csv file

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

dataframe = pandas.DataFrame(data_dict)

dataframe.to_csv("learning/reading-csv/students.csv")
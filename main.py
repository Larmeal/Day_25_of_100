# with open("weather_data.csv") as data:
#     day = data.readlines()

#     print(day)

# import csv

# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperature = []
#     for i in data:python3.8.5 -m pip install pandaspython3.8.5 -m pip install pandas

#         list_day = i
#         if list_day[1] != "temp":
#             temperature.append(list_day[1])

#     print(temperature)

import pandas
# data = pandas.read_csv("weather_data.csv")

# average_tem = data["temp"].mean()
# print(average_tem)

# max_tem = data["temp"].max()
# print(max_tem)

# row_data = data[data.day == "Monday"]
# print(row_data)

# # หา row ที่มีอุณหภูมิสูงที่สุด
# max_row = data[data.temp == max_tem]
# print(max_row)

# # หา temperature ของ Monday แบบ Fahrenheit
# tem_monday = data[data.day == "Monday"]
# tem_monday_Fahrenheit = (tem_monday.temp * 9/5) + 32
# print(tem_monday_Fahrenheit)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_list = data["Primary Fur Color"].to_list()

gray = []
black = []
cinnamon = []
for color in data_list:
    if color == "Gray":
        gray.append(color)
    elif color == "Black":
        black.append(color)
    elif color == "Cinnamon":
        cinnamon.append(color)

count_squirrel = {
    "Fur color": ["gray", "black", "cinnamon"],
    "Count": [len(gray), len(black), len(cinnamon)]
}

csv_data = pandas.DataFrame(count_squirrel)
csv_data.to_csv("Count_Squirrel.csv")

# My teacher version
# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
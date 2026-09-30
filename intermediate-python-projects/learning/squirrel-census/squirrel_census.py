import pandas

data = pandas.read_csv("intermediate-python-projects/tools/squirrel-census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colour = data["Primary Fur Color"]
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
fur_dict = {
    "Fur Colour" : ["Grey", "Cinnamon", "Black"],
    "Count" : [grey_squirrels, red_squirrels, black_squirrels]
}
df = pandas.DataFrame(fur_dict)
df.to_csv("intermediate-python-projects/tools/squirrel-census/squirrel_count.csv")
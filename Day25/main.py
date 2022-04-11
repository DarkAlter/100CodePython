import pandas

def getMaxMean(pandas,csv,value):
    data = pandas.read_csv(csv)
    print(data[value].max())
    print(data[value].mean())

def celcToFareinheit(celc):
    total = (celc * 9/5) + 32
    return float(total)


'''
data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
#ini kondisi ketika mau cari data
#print(data[data.condition == "Sunny"])
#print(data[data.temp == data.temp.max()])

#getMaxMean(pandas,"weather_data.csv", "temp")

monday = data[data.day == "Monday"]
#print(celcToFareinheit(monday.temp))

#create dataframe from scratch
data_dict = {
    "students":["amy", "James", "Angela"],
    "scores":[76,56,65]
}

data2 = pandas.DataFrame(data_dict)
data2.to_csv("newData.csv")

'''
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "colors" : ["Gray", "red","black"],
    "count" : [gray,red,black]
}

print(pandas.DataFrame(data_dict))


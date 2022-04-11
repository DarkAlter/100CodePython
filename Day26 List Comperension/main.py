numbers = [1,2,3]
new_items = []
for n in numbers:
    a = n+1
    new_items.append(a)



new_number = [n+1 for n in numbers]
name = "Angela"
new_list = [n for n in name]
new_range = [n*2 for n in range(1,5)]
names = ["Alex","Beth","Caroline","Dave","Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
#print(short_names)


#squaring numbers
num = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [numbers**2 for numbers in num]
#print(squared_numbers)

#filtering numbers
result = [n for n in num if n%2 == 0]
#print(result)

#data overlap
def openLines(files):
    with open(files) as file:
        contents = file.readlines()
        return contents
result2 = [int(n) for n in openLines("file1.txt") if n in openLines("file2.txt")]
#print(result2)


#dictionary(hashmap) comprehension
import random
names2 = ["Alex","Beth","Caroline","Dave","Elanor", "Freddie"]
student_scores = {student : random.randint(1,100) for student in names2}
#print(student_scores)
passed_students = {student : student_scores[student] for student in names2 if student_scores[student] > 60}
#print(passed_students)

#Dictionary comprehensi ex 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
cutSentence={word:len(word) for word in sentence.split()}
#print(cutSentence)

#Dictionary comprehensi ex 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
def celcToFareinheit(celc):
    total = (celc * 9/5) + 32
    return float(total)

weather_f = {day:celcToFareinheit(temp_c) for (day, temp_c) in weather_c.items()}
#print (weather_f)

#NATO word
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
file = pandas.read_csv("nato_phonetic_alphabet.csv")
newFile = {row.letter:row.code for (index,row) in file.iterrows()}
#print(newFile)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#phonetic = input("")
word = input("")
try:
    arr = [newFile[a.upper()] for a in word]
except KeyError:
    print("String Only")
else:
    print(arr)
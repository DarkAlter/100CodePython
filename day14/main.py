import random
import logo
import data
import os


print(logo.logo)

jumlah_data = len(data.data);

#simpen data pertama dan kedua buat dirandom
firstData = random.randint(0,jumlah_data-1)
SecondData= random.randint(0,jumlah_data-1)

endGame = False
point = 0
while endGame == False:
    #nampung data1

    nama1 = data.data[firstData]["name"]
    follower1 = data.data[firstData]["follower_count"]
    country1 = data.data[firstData]["country"]
    description1 = data.data[firstData]["description"]

    #nampung data2
    nama2 = data.data[SecondData]["name"]
    follower2 = data.data[SecondData]["follower_count"]
    country2 = data.data[SecondData]["country"]
    description2 = data.data[SecondData]["description"]
    
    while nama1 == nama2:
        SecondData= random.randint(0,jumlah_data-1)
        
    clear = lambda: os.system('cls')
    clear()
    
    print(f"{nama1}, {description1}, {country1}")
    print(logo.vs)
    print(f"{nama2}, {description2}, {country2}")
    print(f"your score: {str(point)}")
    
    answer = int(input("which one has the higher follower, 1 or 2? "))
    if answer == 1:
        if follower1 > follower2:
            point +=1
            SecondData= random.randint(0,jumlah_data-1)
        else:
            print("You Lose")
            endGame = True
    else:
        if follower2 > follower1:
            point +=1
            firstData == SecondData
            SecondData= random.randint(0,jumlah_data-1)
        else:
            print("You Lose")
            endGame = True
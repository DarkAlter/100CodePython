import random
import logo
import data

print(logo.logo)

jumlah_data = len(data.data);

#simpen data pertama dan kedua buat dirandom
firstData = random.randint(0,jumlah_data-1)
SecondData= random.randint(0,jumlah_data-1)

#fungsi untuk chek saat dirandom sama atau gak
def checkSama(first, second):
    while first == second:
        if first == second:
            SecondData= random.randint(0,jumlah_data-1)
    return True

            

            

    
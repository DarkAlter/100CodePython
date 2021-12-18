#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
jumlahLetter = len(letters)
jumlahSymbols = len(symbols)




tampungPassword = ""
for huruf in range (1, nr_letters + 1):
    tampungLetters = random.randint(0, jumlahLetter)
    tampungPassword += letters[tampungLetters]
    
for nomor in range (1,nr_numbers + 1):
    tampungNumbers = random.randint(0,9)
    tampungPassword += numbers[tampungNumbers]

for simbol in range(1, nr_symbols+1):
    tampungSymbols = random.randint(0, jumlahSymbols)
    tampungPassword += symbols[tampungSymbols]
    
    
print (tampungPassword)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

tampungPassword = []
#jumlah karakter
jumlahPassword = nr_letters + nr_numbers + nr_symbols
password = ""
for huruf in range (0, nr_letters):
    tampungLetters = random.randint(0, jumlahLetter)
    tampungPassword.append(letters[tampungLetters])
    
for nomor in range (0, nr_numbers ):
    tampungNumbers = random.randint(0,8)
    tampungPassword.append(numbers[tampungNumbers])


for simbol in range(0, nr_symbols):
    tampungSymbols = random.randint(0, jumlahSymbols)
    tampungPassword.append(symbols[tampungSymbols])
    


for karakterPassword in range(0, jumlahPassword):
    karakterAcak = random.randint(0, jumlahPassword-1)
    password += tampungPassword[karakterAcak]
    
print (password)
    

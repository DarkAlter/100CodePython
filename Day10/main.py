import art
import os
def logo():
    logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
    print(logo)

def calculator():
    
    logo()

    operation = {"+":art.add, "-":art.minus, "/":art.divide, "*":art.multiple}

    num1 = int(input("insert first number: "))
    num2 = int(input("insert second number: "))
    operasi = input("pilih operasi: ")
    hasil = operation[operasi](num1,num2)

    print(f"{num1} {operasi} {num2} = {int(hasil)}")

    isContinue = False

    while not isContinue:
        pilihan = input("tekan 'y' untuk melanjutkan dan tekan 'n' untuk selesai: ")
        if pilihan.lower() == "y":
            isContinue = False
        else:
            clear = lambda: os.system('cls')
            clear()
            isContinue = True
            calculator()
        num1 = hasil;
        num2 = int(input("insert next number: "))
        operasi = input("pilih operasi: ")
        hasil = operation[operasi](num1,num2)
        print(f"{num1} {operasi} {num2} = {int(hasil)}")
       
            
calculator()

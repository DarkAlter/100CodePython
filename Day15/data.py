MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def keluarinResources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"water: {int(water)}")
    print(f"milk: {int(milk)}")
    print(f"coffee: {int(coffee)}")

def hitungJumlahKoin(penny, nickel, dime, quarter):
    jumlahPenny = int(penny) * 1
    jumlahNickel = int(nickel)*5
    jumlahDime = int(dime)*10
    jumlahQuarter = int(quarter)*25
    total = (jumlahPenny + jumlahNickel + jumlahDime+jumlahQuarter) / 100
    return total

def masukanKoin(jenis):
    a = input("How many Quarters?")
    b = input("How many dimes?")
    c = input("How many nickels?")
    d = input("How many pennys?")
    tampungHarga = MENU[jenis]["cost"]
    totalHarga = hitungJumlahKoin(d,c,b,a) - tampungHarga
    return totalHarga

def updateResources(jenis):
    if(jenis.lower == "espresso"):
     aer =  resources["water"] - MENU[jenis]["ingredients"]["water"] 
     kopi =  resources["coffee"] - MENU[jenis]["ingredients"]["coffee"] 
     if(aer > 0 and kopi >0):
        updateResource = {
            "water" : aer,
            "coffee": kopi
        }
        resources.update(updateResource)
        return True
     else:
         return False
    else:
        aer =  resources["water"] - MENU[jenis]["ingredients"]["water"] 
        susu = resources["milk"] - MENU[jenis]["ingredients"]["milk"] 
        kopi =  resources["coffee"] - MENU[jenis]["ingredients"]["coffee"]
        if(aer > 0 and kopi >0 and susu >0):
            updateResource = {
            "water" : aer,
            "milk"  :susu,
            "coffee": kopi
            }
            resources.update(updateResource)
            return True
        else:
            return False
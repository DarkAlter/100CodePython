from data import MENU, resources, keluarinResources, masukanKoin,updateResources


isOn = True
while isOn:
    resp = input("What would you like? espresso, latte, or cappucino:")
    if(resp.lower() == "report"):
        keluarinResources()
    elif(resp.lower() == "espresso"):
        harga = masukanKoin(resp.lower())
        if(harga > 0):
            if(updateResources(resp.lower()) == True):
                print(f"Here is change {harga}")
                print(f"Enjoy Your {resp.lower()}")
            else:
                print("Out of Resources of coffee")     
        else:
            print("Your Money is not enough")
    elif(resp.lower() == "latte"):
        harga = masukanKoin(resp.lower())
        if(harga > 0):
            if(updateResources(resp.lower()) == True):
                print(f"Here is change {harga}")
                print(f"Enjoy Your {resp.lower()}")
            else:
                print("Out of Resources of coffee") 
        else:
            print("Your Money is not enough")
    elif(resp.lower() == "cappuccino"):
        harga = masukanKoin(resp.lower())
        if(harga > 0):
            if(updateResources(resp.lower()) == True):
                print(f"Here is change {harga}")
                print(f"Enjoy Your {resp.lower()}")
            else:
                print("Out of Resources of coffee") 
        else:
            print("Your Money is not enough")
    elif(resp.lower() == "off"):
        isOn = False
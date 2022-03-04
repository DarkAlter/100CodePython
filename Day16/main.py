from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
maker = CoffeeMaker()
machine = MoneyMachine()

#Output keluaran Menu Utama
print("Welcome To COffee Machine")
isOn = True
while isOn:
    resp = input(f"What would you want?{menu.get_items()}")

    if(resp.lower() == "report"):
        maker.report()
    elif(resp.lower() == "off"):
       isOn = False
    else:
        if(maker.is_resource_sufficient(menu.find_drink(resp.lower())) and machine.make_payment(menu.find_drink(resp.lower()).cost)):
            maker.make_coffee(menu.find_drink(resp.lower()))
        
    
    
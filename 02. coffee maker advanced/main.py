from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


macchinetta = CoffeeMaker()
macchinetta_soldi = MoneyMachine()
lista_menu = Menu()
ord = 1

while ord == 1:
    elemento = input(f"abbiamo a disposizione {lista_menu.get_items()}, che cosa vorresti?")
    ordine = lista_menu.find_drink(elemento)

    if ordine == None:
        ord = 0
        break

    fattibilita = macchinetta.is_resource_sufficient(ordine)
    if not fattibilita:
        print("risorse insufficenti")

    else:
        print(f"il costo è di {ordine.cost} dollari")

        if macchinetta_soldi.make_payment(ordine.cost):
            macchinetta.make_coffee(ordine)
            macchinetta.report()
            macchinetta_soldi.report()







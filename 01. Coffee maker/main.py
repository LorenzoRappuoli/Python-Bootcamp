# IMPORTA I DIZIONARI CON I VALORI

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

# CREA LE FUNZIONI


def chiedi_cliente():
    _richiesta = input("Cosa vuoi ordinare? (espresso,latte,cappuccino)")
    while _richiesta not in  ["espresso","latte","cappuccino"]:
        _richiesta = input("l'elemento non esiste, cosa vuoi ordinare? (espresso,latte,cappuccino)")
    return _richiesta


def monete():
    cinquantino =  int(input("Quante monete da 50 centesimi? "))*0.5
    euro = int(input("Quante monete da 1 euro? "))
    due_euro = int(input("Quante monete da 2 euro? "))*2
    return cinquantino + euro + due_euro


def pagamento (ric):
    global MENU
    procediamo = 0
    costo = MENU[ric]['cost']
    print(f"il costo per {ric} è pari a {costo} euro")
    inserito = monete()
    if inserito < costo:
        print("il valore non è sufficiente, ordine annullato")
    elif inserito > costo:
        print(f"il resto è pari a {inserito - costo}")
        procediamo = 1
    else:
        procediamo = 1
    return procediamo


def check_ingredienti (richiesta):
    """

    :param richiesta: prodotto da ricevere
    :return: se è fattibile o meno
    """
    global MENU
    global resources
    procediamo = 1

    try:
        latte = MENU[richiesta]["ingredients"]["milk"]

    except:
        latte = 0

    acqua = MENU[richiesta]["ingredients"]["water"]
    caffe = MENU[richiesta]["ingredients"]["coffee"]

    if resources["water"] < acqua:
        print("acqua non sufficiente, ordine rimborsato")
        procediamo = 0
    if resources["milk"] < latte:
        print("latte non sufficiente, ordine rimborsato")
        procediamo = 0
    if resources["coffee"] < caffe:
        print("caffè non sufficiente, ordine rimborsato")
        procediamo = 0

    if procediamo == 1:
        resources["water"] = resources["water"] - acqua
        resources["milk"] = resources["milk"] - latte
        resources["coffee"] = resources["coffee"] - caffe

    return procediamo



def ordine_cliente ():
    ric_utente = chiedi_cliente()
    procediamo = pagamento(ric_utente)

    if procediamo == 0:
        print("ordine annullato")
        return

    procediamo = check_ingredienti(ric_utente)

    if procediamo == 0:
        print("ordine terminato")
        return

    if procediamo == 1:
        print(f"ritirare {ric_utente}")
        return


ordini_fila = True

while ordini_fila:
    ordine_cliente()
    print("---------------------")
    print(resources)
    print("---------------------")
    if input("Ordinare altro? SI/NO ").lower() == "NO":
        ordini_fila = False




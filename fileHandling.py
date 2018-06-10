fileName = 'test.txt' # Het bestand waarin word geschreven
linebreak = '\n' # enter in een variable zetten voor duidelijkheid

def getItemsFromFile(): # Bestand Uitlees functie
    try:
       file = open(fileName, "r") # proberen het bestand te openen met als regel: r - Read
    except:
        return [] # Als het niet lukt, leeg array terug geven aan de functie uitkomst

    listOfItems = [] # Array aanmaken voor de gevonden gegevens
    for item in file: # Door elke regel van het bestand heen loopen
        listOfItems.append(item.strip(linebreak).split(', ')) # linebreak weghalen, en aan het einde van de array toevoegen.

    file.close() # bestand afsluiten
    return listOfItems # Array met gelezen regels/items terug geven aan de functie uitkomst

def writeItemsToFile(listOfItems):  # Bestand Schrijf functie
    try:
        file = open(fileName, "w") # proberen het bestand te openen met als regel: w - Write
    except:
        return False # Lukt het niet dan False teruggeven aan de functie uitkomst

    for item in listOfItems: # Door alle items loopen die aan deze functe zijn meegegeven
        file.write((', '.join(map(str, item))) + linebreak) # Van ieder item een string maken, en een linebreak achter het item plaatsen 

    file.close() # bestand afsluiten
    return True # True teruggeven aan de functie, omdat het is uitgevoerd

items = [['a,99,22'], ['b,34,dd'], ['c,5,21']] # Array met items
writeItemsToFile(items) # Array met items in het bestand schrijven (roept de functie hierboven benoemd aan)
items = getItemsFromFile() # items uitlezen met de bovenstaande functie en in de items variable zetten
print(items) # items printen

# # Willkommen zum Ordnungsrechner 
# ## Der Ordnungsrechner berechnet die Ordnung eines bestimmten Elements in einer Gruppe mit der Multiplikation und/oder Addition als Verknüpfung!

# Initialisierung

modulo = None
element = None
Verknüpfung = None


# Fehlerabfrage und Eingabe

while(type(modulo) != int):
    try:
        print("\nBitte geben Sie eine gültige Ganzzahl ein.")
        modulo = int(input("\nModulo n der Restklasse: "))
    except Exception as e:
        print("\n\n\nFehlercode: ", e)

while(type(element) != int):
    try:
        print("\nBitte geben Sie eine gültige Ganzzahl ein.")
        element = int(input("\nElement g, deren Ordnung bestimmt werden muss: "))
    except Exception as e:
        print("\n\n\nFehlercode: ", e)

while(Verknüpfung != "+" and Verknüpfung != "*" and Verknüpfung != "Beide"):
    try:
        print("\nBitte geben Sie eine gültige Verknüpfung (+, *, Beide) ein.")
        Verknüpfung = input("\nVerknüpfung, welche in der Gruppe herrscht: ")
    except Exception as e:
        print("\n\n\nFehlercode: ", e)


# ### Multiplikative Verknüpfung:
# ##### Teileranzahl und Teiler von n-1 bestimmen:

def Ordnungsrechner(modulo, element, Verknüpfung):
    if(Verknüpfung == "*" or Verknüpfung == "Beide"):
        print("\nMultiplikative Verknüpfung\n")
        
        teileranzahl = 0
        teiler = []
        zaehler = 0


        for zaehler in range(1, int(((modulo-1)/2)+1)): # Die for-Schleife findet alle echten Teiler von n-1 und die 1
            if((modulo-1)%zaehler == 0):
                teileranzahl = teileranzahl + 1; # Weiterer Teiler wurde gefunden
                teiler.append(zaehler) #Teiler wird zur Teilerliste hinzugefügt
                #print("Teileranzahl: ", teileranzahl)
                #print("Die Teiler sind: ", teiler)

        # Dieser Abschnitt fügt noch den unechten Teiler n-1 zu den Teilern hinzu
        teileranzahl = teileranzahl + 1
        teiler.append((modulo-1))

        print("Teileranzahl: ", teileranzahl)
        print("Die Teiler sind: ", teiler)


    # ##### Nun wird nach der Ordnung des Elementes g geschaut:


        index = 0
        ordnung = None
        ergebnis = None


        for index in range(teileranzahl):
            ergebnis = (element**teiler[index])%modulo
            if(ergebnis == 1):
                ordnung = teiler[index]
                break
                
        if(ordnung == None): # Abfangabfrage, wenn sich die Ordnung des Elements nicht berechnen lässt, da z.b. die Eingabe falsch war oder die Ordnung nicht errechenbar ist in dem Körper
            print("\n\n\nBei der Berechnung der Ordnung ist entweder ein Fehler unterlaufen oder es kann keine Ordnung für dieses Element in dem Körper mit einer multiplikativen Verknüpfung berechnet werden. Überprüfen Sie ihre Eingabe oder kontaktieren Sie den Hersteller")
        else:
            print("\nDie Ordnung des Elements ", element, " in der Restklasse ", modulo, " mit der multiplikativen Verknüpfung ist: ", ordnung)


    # ### Additive Verknüpfung:


    if(Verknüpfung == "+" or Verknüpfung == "Beide"):
        print("\nAdditive Verknüpfung\n")

        ordnung = None
        ergebnis = None


        for ordnung in range(1, modulo):
            ergebnis = (element*ordnung)%modulo
            if(ergebnis == 0):
                #print(ordnung)
                break


        if(ordnung == None): # Abfangabfrage, wenn sich die Ordnung des Elements nicht berechnen lässt, da z.b. die Eingabe falsch war oder die Ordnung nicht errechenbar ist in dem Körper
            print("\n\n\nBei der Berechnung der Ordnung ist entweder ein Fehler unterlaufen oder es kann keine Ordnung für dieses Element in dem Körper mit einer multiplikativen Verknüpfung berechnet werden. Überprüfen Sie ihre Eingabe oder kontaktieren Sie den Hersteller")
        elif(ergebnis != 0):
            print("\nDas Element ", element, " in der Restklasse ", modulo, " mit der additiven Verknüpfung hat keine Ordnung")
        else:
            print("\nDie Ordnung des Elements ", element, " in der Restklasse ", modulo, " mit der additiven Verknüpfung ist: ", ordnung)

Ordnungsrechner(modulo, element, Verknüpfung)
störstaTal = 0
lista = [] # Skapar en lista där sifforrna sparas
print("Hur många siffror finns i listan?")
antal = int(input("")) # Skriver hur många tal det ska vara i listan
for x in range(antal): # Kör koden "x" antal gånger
    tal = int(input("Skriv ett tal: ")) # Skriver in talen
    lista.append(tal) #Lägger till talet som skrivits i listan
print(lista)
for g in lista:
    if g > störstaTal: # Kör alla tal
        störstatalet = g # Om g är större än störstatalet
print("största talet är: ", störstaTal)
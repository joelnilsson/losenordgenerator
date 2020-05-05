störstaTal = 0
lista = []
print("Hur många siffror finns i listan?")
antal = int(input(""))
for x in range(antal):
    tal = int(input("Skriv ett tal: "))
    lista.append(tal)
print(lista)
for g in lista:
    if g > störstaTal:
        störstatalet = g
print("största talet är: ", störstaTal)
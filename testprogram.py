import csv, subprocess, platform, os, random, string

osys = platform.system()
running = True
meny = 0
chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars2 = "0123456789"
chars3 = "!#/()=#"


# def generatePass(length=):

def getFileLocation():
    working = False
    while working == False:
        print('Skriv sökvägen till CSV filen.')
        csvLocation = input("csv: ")
        if os.path.isfile(csvLocation) == False:
            print("Filen existerar inte, vänligen testa igen.")
        elif os.path.isfile(csvLocation) == True:
            print("Filen existerar.")
            working = True
            return csvLocation
        else:
            print("gg")

def passwordGen(length=8):
    password = ''
    password += random.choice(chars)
    password += random.choice(chars1)
    password += random.choice(chars2)
    password += random.choice(chars3)
    for cat in range(length-4):
        cat = random.randint(1,4)
        if cat == 1:
            password += random.choice(chars)
        elif cat == 2:
            password += random.choice(chars1)
        elif cat == 3:
            password += random.choice(chars2)
        else:
            password += random.choice(chars3)
    return password

def addUser(os = osys):
    if osys == 'Linux':
        cmd = "linux add user"
    else:
        cmd = f'New-ADUSer ' 
    returnedValue = subprocess.call(cmd, shell=True)
    if returnedValue >= 1:
        print(f"Något gick fel.\n Returned Value: {returnedValue}")


print(f'''Välkommen,
Du kör operativsystemet {osys}.''')

while running:
    if meny == 0:
        try:
            print("\nMeny\nLägg till användare [1]\nRadera användare [2]\nAvsluta [3]")
            meny = int(input("Val: "))
            if  meny == 0 or meny >= 4:
                print("Välj ett av de tillgänliga alternativen.")
                meny = 0
        except:
            print("Välj ett av de tillgänliga alternativen.")
            meny = 0
    if meny == 1:
        correctCSVLocation = getFileLocation()
        with open (correctCSVLocation, newline='') as csvFile:
            readFile = csv.DictReader(csvFile)
            for row in readFile:
                print(row)
                print(f'Lösenord: {passwordGen()}')

        meny = 0

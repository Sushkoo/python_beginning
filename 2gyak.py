import math
#print("Pi értéke = {pi:.2f}".format(pi = math.pi))

#1. feladat: Számológép

szam1 = input("Add meg az első számot: ")
szam2 = input("Add meg a második számot: ")
muvelet = input("Add meg a műveletet (+, -, *, /): ")

if muvelet == '+':
    szam1 = float(szam1)
    szam2 = float(szam2)
    eredmeny = szam1 + szam2
elif muvelet == '-':
    szam1 = float(szam1)
    szam2 = float(szam2)
    eredmeny = szam1 - szam2
elif muvelet == '*':
    szam1 = float(szam1)
    szam2 = float(szam2)
    eredmeny = szam1 * szam2
elif muvelet == '/':
    szam1 = float(szam1)
    szam2 = float(szam2)
    if szam2 != 0:
        eredmeny = szam1 / szam2
    else:
        eredmeny = "Hiba: Nullával való osztás!"
else:
    eredmeny = "Hiba: Érvénytelen művelet!"

print("{szam1} {muvelet} {szam2} = ".format(szam1=szam1, muvelet=muvelet, szam2=szam2), eredmeny)

#2. feladat: masodfoku egyenlet

a = float(input("Add meg az 'a' együtthatót (nem lehet 0): "))
b = float(input("Add meg a 'b' együtthatót: "))
c = float(input("Add meg a 'c' együtthatót: "))

if a == 0:
    print("Hiba: 'a' nem lehet 0.")
else:
    d = b**2 - 4*a*c  # Diszkrimináns
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Két valós gyök van: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif d == 0:
        x = -b / (2*a)
        print(f"Egy valós gyök van: x = {x:.2f}")
    else:
        print("Nincs valós gyök.")

#3. feladat: Írjunk programot, mely egy beolvasott dátumnak megfelelően kiírja a hónap napjainak a számát, szökévekre is figyelve.

while True:
    try:
        ev = int(input("Add meg az évet: "))
        honap = int(input("Add meg a hónapot: "))

        if ev > 0 and honap > 0:
            if honap > 12:
                print("A hónap nem lehet nagyobb 12-nél.\n")
                continue

            napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            if ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0):
                napok[1] = 29

            print(f"A {honap}. hónapban {napok[honap - 1]} nap van.\n")
            break

        else:
            print("Az évnek és hónapnak pozitív számoknak kell lennie.\n")

    except ValueError as e:
        print(f"Hibás bemenet: {e}\n")


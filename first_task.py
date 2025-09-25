import math

# Első feladat: Kör terület és kerület kiszámítása (hibakezelés)

#Kerület: 2 * r * π
#Terület: r² * π

while True:
    try:
        kor_sugara = float(input("Add meg a kör sugarát: "))
    
        if kor_sugara > 0:
            kor_terulete = math.pi * kor_sugara ** 2
            kor_kerulete = 2 * math.pi * kor_sugara
            print(f"A kör területe: {kor_terulete:.2f}")
            print(f"A kör kerülete: {kor_kerulete:.2f}\n")
            break

        else:
            print("A sugárnak pozitív számnak kell lennie.\n")

    except ValueError as e:
        print(f"Hibás bemenet: {e}\n")
        
# Második feladat Két egész szám számtani és mértani közepének kiszámítása (hibakezelés): 

#Számtani közép képlete: (a + b) / 2
#Mértani közép képlete: √(a * b)

while True:
    try:
        a = float(input("Add meg az első számot: "))
        b = float(input("Add meg a második számot: "))

        if a > 0 and b > 0:
            szamtani_kozepe = (a + b) / 2
            mertani_kozepe = math.sqrt(a * b)
            print(f"A számtani közepe: {szamtani_kozepe:.2f}")
            print(f"A mértani közepe: {mertani_kozepe:.2f}\n")
            break

        else:
            print("Mindkét számnak pozitívnak kell lennie.\n")

    except ValueError as e:
        print(f"Hibás bemenet: {e}\n")




#Extra

# Harmadik feladat: Háromszög megrajzolható e a megadott oldalakból (hibakezelés)

while True:
    try:
        a = float(input("Add meg az első oldal hosszát: "))
        b = float(input("Add meg a második oldal hosszát: "))
        c = float(input("Add meg a harmadik oldal hosszát: "))

        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                print("A háromszög megrajzolható ezekből az oldalakból.\n")
            else:
                print("A háromszög nem rajzolható meg ezekből az oldalakból.\n")
            break

        else:
            print("Az oldalak hosszának pozitív számoknak kell lennie.\n")

    except ValueError as e:
        print(f"Hibás bemenet: {e}\n")


# Negyedik feladat: Háromszög rajzolása csillagokkal (hibakezelés)

while True:
    try:
        magassag = int(input("Add meg a háromszög magasságát (pozitív egész szám): "))

        if magassag > 0:
            for i in range(1, magassag + 1):
                print(' ' * (magassag - i) + '*' * (2 * i - 1))
            print()
            break

        else:
            print("A magasságnak pozitív egész számnak kell lennie.\n")

    except ValueError as e:
        print(f"Hibás bemenet: {e}\n")
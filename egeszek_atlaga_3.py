osszeg = 0
darab = 0

while True:
    try:
        szam = int(input())
        if szam == 0:
            break
        osszeg += szam
        darab += 1
    except ValueError:
        print("Egész számot adj meg.")
        exit()

if darab == 0:
    atlag = 0
else:
    atlag = osszeg / darab

print(f"{atlag:.2f}")

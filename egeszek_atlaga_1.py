try:
    n = int(input())
    osszeg = 0

    for i in range(n):
        szam = int(input())
        osszeg += szam

    atlag = osszeg / n

    print(f"{atlag:.2f}")
except ValueError:
    print("Csak egész számot adj meg.")
    exit()

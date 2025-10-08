try:
    n = int(input())
    if n <= 0:
        print("Csak pozitív egész számot írhatsz be.")
except ValueError:
    print("Csak pozitív egész számot írhatsz be.")
    exit()

max = 0
i = 1

while n > 0:
    try:
        szam = int(input())
        if szam > max:
            max = szam
        n -= 1
        i += 1
    except ValueError:
        print("Csak egész számot írhatsz be.")
        exit()

print(max)

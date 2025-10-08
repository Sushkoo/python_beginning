while True:
    pont = int(input())

    if pont < 0:
        break

    if pont >= 80:
        print("jeles")
    elif pont >= 70:
        print("jo")
    elif pont >= 60:
        print("kozepes")
    elif pont >= 50:
        print("elegseges")
    else:
        print("elegtelen")

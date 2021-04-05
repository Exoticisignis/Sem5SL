def listOfPrimes(start,length):
    primeList = []
    while len(primeList) != length:
        start += 1
        prime = True
        for i in range(2, int(start/2) + 1):
            if start % i == 0:
                prime = False
        if prime:
            primeList.append(start)

    return ", ".join(str(x) for x in primeList)

if __name__ == '__main__':
    start = input("First number: ")
    length = input("How many: ")
    if start.isdigit() and length.isdigit():
        print(listOfPrimes(int(start),int(length)))
    else :
        print("Wrong input")
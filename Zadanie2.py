def isPrime(n):
    while True:
        n +=1
        prime = True
        for i in range(2, int(n/2) + 1):
            if n % i == 0:
                prime = False
        if prime:
            return n


if __name__ == '__main__':
    line = input("Put your number: ")
    if line.isdigit():
        print (isPrime(int(line)))
    else:
        print ("Wrong input")

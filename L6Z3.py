import time
if __name__ == '__main__':
    country = input('Set country: ')
    start = time.time()
    file = open('Covid.txt', 'r')
    sum = 0
    for line in file:
        argList = line.split('\t')
        if len(argList) >= 6:
            if argList[4].isdigit() and argList[6] == country:
                sum += int(argList[4])
    fulltime = time.time() - start
    print(sum)
    print(fulltime)
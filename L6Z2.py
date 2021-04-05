import time


def zadanie2():
    start_time = time.time()
    file = open('/Users/matveidzebysh/Desktop/Skrypty/PyCharm/Covid.txt', 'r')
    sum = 0
    for line in file:
        argList = line.split('\t')
        if len(argList) >= 4:
            if argList[4].isdigit():
                sum += int(argList[4])
    full_time = time.time() - start_time
    print(sum)
    print(full_time)


def zadanie3():
    country = input('Set country: ')
    start_time = time.time()
    file = open('Covid.txt', 'r')
    sum = 0
    for line in file:
        argList = line.split('\t')
        if len(argList) >= 6:
            if argList[4].isdigit() and argList[6] == country:
                sum += int(argList[4])
    full_time = time.time() - start_time
    print(sum)
    print(full_time)


if __name__ == '__main__':
    zadanie2()
    zadanie3()

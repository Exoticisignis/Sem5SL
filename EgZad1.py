def getListFromFile():
    file = open('/Users/matveidzebysh/Desktop/Skrypty/PyCharm/Covid.txt', 'r')
    rlist = list(map(lambda x: x.split('\t'), file.read().split('\n')[1:]))
    return rlist

def getWorstDays(data):
    results = { 1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{},11:{},12:{}}
    for m in results:
        for line in data:
            if (len(line)) > 6:
                if int(line[2]) == m:
                    results[m][line[1]] = 0
    # musiałem zrobić dwa bloki bo inaczej miałem KeyError
    for m in results:
        for line in data:
            if (len(line)) > 6:
                if int(line[2]) == m:
                    results[m][line[1]] += int(line[5])
    for k in results.keys():
        maximum = [0, 0]
        for day, deaths in results[k].items():
            if deaths > maximum[1]:
                maximum = [day, deaths]
        print('Najgorszy dzien: '+str(maximum[0])+' , w miesiecu: '+str(k)+' , liczba zgonów: '+str(maximum[1]))


def printDuplicatedData(data):
    res = {}
    for line in data:
        if (len(line)) > 6:
            sline = ''
            for word in line:
                sline += " "+word
            if sline in res.keys():
                res[sline] += 1
            else:
                res[sline] = 1
    for k in res.keys():
        if res[k] > 1:
            print(k+" ; Liczba wystąpień: " + str(res[k]))

if __name__ == '__main__':
    data = getListFromFile()
    getWorstDays(data)
    printDuplicatedData(data)
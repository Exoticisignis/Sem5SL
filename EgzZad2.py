def getListFromFile():
    file = open('/Users/matveidzebysh/Desktop/Skrypty/PyCharm/Covid.txt', 'r')
    rlist = list(map(lambda x: x.split('\t'), file.read().split('\n')[1:]))
    return rlist

def getRequired(query):
    request = query.split(' ')
    cases = 0
    deaths = 0
    if len(request) != 3:
        raise AttributeError('Input must be consist of 3 elements: day(from) day(to) country')
    if request[1] < request[0]:
        raise AttributeError('First day input must be less then second day input')
    data = getListFromFile()
    for line in data:
        if int(line[1]) > int(request[0] and int(line[1]) < int(request[1])):
            if line[6] == request[2]:
                cases += int(line[4])
                deaths += int(line[5])
    print('Liczba zachorowan: '+str(cases))
    print('Liczba zgonow: '+ str(deaths))

if __name__ == '__main__':
    while True:
        query = input()
        if query == 'break':
            break
        getRequired(query)
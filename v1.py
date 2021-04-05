from Tools import getListFromFile, filterSim


def location(arg, data):
    result = []
    country = -1
    continent = -1
    if arg == 'all':
        return data
    '''
    for i in data:
        continent = filterSim(arg, i[10])
        country = filterSim(arg, i[6])
    if continent != -1:
        for i in data:
            if i[10] == continent:
                result.append((i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    if country != -1:
        for i in data:
            if i[10] == country:
                result.append((i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    '''
    for value in data:
        if value[6] == arg or value[10] == arg:
            result.append((value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8],
                           value[9], value[10]))
    if len(result) == 0:
        raise Exception('Bad argument for country or continent')
    return result


def date(arg, data):
    months = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien',
              'pazdziernik', 'listopad', 'grudzien']
    result = []
    if arg == 'all':
        return data
    check = False
    month = -1
    for i in months:
        if i == arg:
            check = True
            month = months.index(i) + 1
    if check:
        result = list(filter(lambda x: int(x[2]) == month, data))
        return result
    if type(arg) == list:
        if not arg[0].isnumeric() or int(arg[0]) >= 32 or int(arg[0]) < 0:
            raise Exception('Day must be a valid number.')
        for i in months:
            if i == arg[1]:
                check = True
                month = months.index(i) + 1
            if check:
                result = list(filter(lambda x: x[1] == arg[0] and int(x[2]) == month, data))
    if len(result) == 0:
        raise Exception('Bad date argument')
    return result


def cases(arg, data):
    result = []
    if arg == 'zgony':
        for value in data:
            result.append((value[0], value[5], value[6], value[10]))
        result.sort(key=lambda x: x[2])
        result.sort(reverse=True, key=lambda x: int(x[1]))
        return '{:>10} {:>20} {:>20} {:>23} \n'.format('Data', 'Zgony', 'Kraj', 'Kontynent') + '\n'.join(
            '{:>10} {:>15} {:>20} {:>20}'.format(x[0], x[1], x[2], x[3]) for x in result)
    if arg == 'zachorowania':
        for value in data:
            result.append((value[0], value[4], value[6], value[10]))
        result.sort(key=lambda x: x[2])
        result.sort(reverse=True, key=lambda x: int(x[1]))
        return '{:>10} {:>20} {:>20} {:>20} \n'.format('Data', 'Wypadki', 'Kraj', 'Kontynent') + '\n'.join(
            '{:>10} {:>20} {:>20} {:>20}'.format(x[0], x[1], x[2], x[3]) for x in result)


def proceed_arguments(request, data):
    if request == '?':
        return 'Use: <kraj|kontynent|all> <zgony|zachorowania> <dzien|miesiac|all> as input format or exit to finish'
    request = request.split(' ')
    if 3 > len(request) or len(request) > 4:
        raise Exception('Invalid number of arguments.')
    l0 = location(request[0], data)
    if len(request) == 4:
        l1 = date(request[2:4],l0)
    else:
        l1 = date(request[2],l0)
    l2 = cases(request[1], l1)
    return l2


if __name__ == '__main__':
    data = getListFromFile()
    while True:
        request = input('Enter request: ')
        if request == 'exit':
            break
        try:
            print(proceed_arguments(request, data))
        except Exception as err:
            print(err)

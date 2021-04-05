list = [7, 'x', 'y', 6, "uaua", 9, 10, 99]

def process(list):
    new_list = [i for i in list if isinstance(i, int)]
    summ = sum(new_list)
    length = len(new_list)
    average = float(summ / length)
    minn = min(new_list)
    maxx = max(new_list)
    variance = calc_variance(new_list, length, average)
    result = ("Długość: "+str(length),"Średnia wartość: "+str(average),"Wariancja: "+str(variance),"Min: "+str(minn),"Max: "+ str(maxx))
    return result

def calc_variance(calc_list, length, ave):
    var = 0
    for i in calc_list:
        var += float((i - ave) ** 2)
    return var / length

if __name__ == '__main__':
    print(process(list))

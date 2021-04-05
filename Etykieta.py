from Znaczniki import Znaczniki

class Etykieta:
    def __init__(self, string_list):
        self.__znacznik = Znaczniki()
        for string in string_list:
            self.__znacznik.addString(string)

    def addString(self, string):
        return self.__znacznik.addString(string)

    def getList(self):
        return self.__znacznik.getList()

    def __add__(self, other):
        if isinstance(other, Etykieta):
            tmp = Etykieta(self.getList())
            for i in other.getList():
                tmp.addString(i)
            return tmp
        return self.__znacznik

    def __mul__(self, other):
        if isinstance(other, Etykieta):
            l1 = list(self.getList())
            l2 = list(other.getList())
            tmp = list(value for value in l1 if value in l2)
            temp = Etykieta(tmp)
            return temp
        return self.__znacznik

    def __sub__(self, other):
        if isinstance(other, Etykieta):
            tmp = Etykieta([])
            for i in self.getList():
                if i not in other.getList():
                    tmp.addString(i)
            return tmp
        return self.__znacznik

    def __eq__(self, other):
        if isinstance(other, Etykieta):
            return self.getList() == other.getList()
        return False

    def __le__(self, other):
        if isinstance(other, Etykieta):
            bool = True
            for i in self.getList():
                if i not in other.getList():
                    bool = False
            return bool
        return False

    def __ge__(self, other):
        if isinstance(other, Etykieta):
            bool = True
            for i in other.getList():
                if i not in self.getList():
                    bool = False
            return bool
        return False

    def __ne__(self, other):
        if isinstance(other, Etykieta):
            l1 = list(self.getList())
            l2 = list(other.getList())
            tmp = list(value for value in l1 if value in l2)
            return tmp == []
        return False

    def save(self, filename):
        f = open(filename, 'w+')
        for i in self.getList():
            f.write(i + '\n')
        f.close()

    def open(self, filename):
        try:
            with open(filename, 'r') as f:
                fl = f.read().split('\n')
                for i in fl:
                    if i != '':
                        self.addString(i)
        except FileNotFoundError:
            print("file {} does not exist".format(filename))

    def __str__(self):
        return ', '.join(self.__znacznik.getList())
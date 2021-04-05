from Tools import LevSim
import re

class Znaczniki:
    __MAX_DL = 20
    __MIN_DL = 3
    def __init__(self):
        self.__string_list = []

    def getList(self):
        return self.__string_list

    def addString(self, ciag):
        if ciag in self.__string_list:
            raise Exception('Ciag juz jest w tabele')
        if not re.match("^[a-zA-Z0-9_]+$", ciag) or ciag.count('_') > 2 or len(ciag) > self.__MAX_DL or len(ciag) < self.__MIN_DL:
            raise Exception('Bledny ciag')
        self.__string_list.append(ciag)

    def getString(self, ciag, odleglosc):
        rlist = []
        for s in self.__string_list:
            if LevSim(ciag, s) < odleglosc:
                rlist.append(s)
        return rlist

    def getAccepted(self, lista_ciagow):
        rlist = []
        for s in lista_ciagow.getList():
            if s in self.__string_list:
                rlist.append(s)
        return rlist

    def getRejected(self, lista_ciagow):
        rlist = []
        for s in lista_ciagow.getList():
            if s not in self.__string_list:
                rlist.append(s)
        return rlist

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
                    if i!='':
                        self.addString(i)
        except FileNotFoundError:
            print("file {} does not exist".format(filename))

    def __str__(self):
        return ', '.join(self.__string_list)

import datetime

class Osoba:
    __uId = 1

    def __init__(self, name, surname, birthDate,):
        self.__surname = surname
        self.__birthDate = birthDate
        if type(name) is list and len(name) > 3:
            raise Exception('Max length : 3 in Osoba.__init__')
        if type(name) is list:
            self.__nameList = name
        else :
            self.__nameList = [name]
        self.__id = Osoba.__uId
        Osoba.__uId += 1
        try:
         self.__birthDate = datetime.datetime.strptime(birthDate, '%Y-%m-%d').date()
        except ValueError:
            print('Bad date format, must be: yyyy-mm-dd')
        
    @property    
    def __age(self):
        today = datetime.date.today()
        return int(today.year - self.__birthDate.year)

    def getAge(self):
        return self.__age

    def getSurname(self):
        return self.__surname

    def __str__(self):
        myString = str(self.__id) + ', ' + self.__surname + ', '
        for name in self.__nameList:
            myString += name + ', '
        myString += str(self.__birthDate) + ', ' + str(self.__age)
        return myString

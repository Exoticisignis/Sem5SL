from Osoba import Osoba

class Student(Osoba):
    def __init__(self, name, surname, birthDate):
        Osoba.__init__(self, name=name, surname=surname, birthDate=birthDate)
        self.__markList = []

    def addMark(self, subject_code, subject_mark):
        if 2 > float(subject_mark) > 5.5:
            return False

        for code, mark in self.__markList:
            if code == subject_code and mark != '2.0':
                return False
        self.__markList.append((subject_code, subject_mark))
        return True

    def getAverage(self):
        sum = 0
        for code, mark in self.__markList:
            sum += float(mark)

        return sum / len(self.__markList)

    def __str__(self):
        return super().__str__() + ', Number of marks: ' + str(len(self.__markList))
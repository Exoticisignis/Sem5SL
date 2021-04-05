from Osoba import Osoba
from datetime import date

class Pracownik(Osoba):
    def __init__(self, name, surname, birthDate):
        Osoba.__init__(self, name=name, surname=surname, birthDate=birthDate)
        self.__publicationList = []

    def addPublication(self, pubYear, pubPoints):
        bYear = date.today().year - self.getAge()
        if bYear <= pubYear <= date.today().year:
            self.__publicationList.append((int(pubYear), int(pubPoints)))

    def pointsFor4Years(self):
        sum = 0
        for temp in self.__publicationList:
            if date.today().year - temp[0] <= 3:
                sum += temp[1]
        return sum

    @property
    def __yearsWithoutPublications(self):
        years_dict = {}
        return_years_list = []
        bYear = date.today().year - self.__age
        for temp in self.__publicationList:
            if temp[0] not in years_dict.keys():
                years_dict[temp[0]] = 1

        for year in range(bYear + 18, date.today().year + 1):
            if year not in years_dict.keys():
                return_years_list.append(year)

        return return_years_list

    def getYearsWithoutPubs(self):
        return self.__yearsWithoutPublications

    def __str__(self):
        return super().__str__() + ', Number of publications: ' + str(len(self.__publicationList))

'''if __name__ == '__main__':
    p = Pracownik('Name', 'Surname', '1976-07-09')
    p.addPublication(2004, 44)
    p.addPublication(2005, 55)
    p.addPublication(2006, 77)
    print(p)
    (p.yearsWithoutPublications)'''

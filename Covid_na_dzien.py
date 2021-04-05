class Covid_na_dzien:
    def __init__(self, day, month, year, cases, deaths):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__cases = int(cases)
        self.__deaths = int(deaths)

    @classmethod
    def object_from_line(cls, line):
        temp_data = line.split()
        if len(temp_data) >= 6:
            return cls(temp_data[1], temp_data[2], temp_data[3], temp_data[4], temp_data[5])

    @classmethod
    def object_from_data(cls, date, cases, deaths):
        date = date.split(".")
        return cls(date[0], date[1], date[2], cases, deaths)

    def __str__(self):
        return self.day + '/' + self.month + '/' + self.year + '\t' + str(self.cases) + '\t' + str(self.deaths)

    def get_date(self):
        return self.day + '/' + self.month + '/' + self.year + '\t'

    def get_cases(self):
        return self.cases

    def get_deaths(self):
        return self.deaths


if __name__ == '__main__':
    d1 = Covid_na_dzien('22', '11', '2020', '814', '12')
    d2 = Covid_na_dzien.object_from_line('11.08.2020	11	8	2020	0	0	Afghanistan	AF	AFG	38041757	Asia	1,80328159')
    d3 = Covid_na_dzien.object_from_data('22.11.2020', '814', '12')
    print(d1)
    print(d2)
    print(d3)
    print(d1.get_date())
    print(d2.get_cases())
    print(d3.get_deaths())
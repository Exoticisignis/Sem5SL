from Covid_na_dzien import Covid_na_dzien

class Przypadki_kraj:
    def __init__(self, country_code):
        self.country_code = country_code
        self.day_list = []
        self.cases_sum = 0
        self.deaths_sum = 0

    def day_dont_exist(self, date):
        temp_day = Covid_na_dzien.object_from_data(date, 0, 0)
        for day in self.day_list:
            if day.get_date() == temp_day.get_date():
                return False
        return True

    def add_day_data(self, date, cases, deaths):
        if self.day_dont_exist(date):
            temp_day = Covid_na_dzien.object_from_data(date, cases, deaths)
            self.day_list.append(temp_day)
            self.deaths_sum += deaths
            self.cases_sum += cases
            return True
        return False

    @classmethod
    def object_from_data(cls, date, cases, deaths, country_code):
        temp_obj = cls(country_code)
        temp_obj.add_day_data(date, cases, deaths)
        return temp_obj

    def add_day_line(self, line):
        temp_day = Covid_na_dzien.object_from_line(line)
        data_from_line = line.split()
        if len(data_from_line) >= 9:
            if data_from_line[8] != self.country_code:
                return False
            for day in self.day_list:
                if day.get_date() == temp_day.get_date():
                    return False
            self.day_list.append(temp_day)
            self.cases_sum += temp_day.get_cases()
            self.deaths_sum += temp_day.get_deaths()
            return True
        return False

    @classmethod
    def object_from_line(cls, line):
        data_from_line = line.split()
        if len(data_from_line) >= 9:
            temp_obj = cls(data_from_line[8])
            temp_obj.add_day_line(line)
            return temp_obj

    def __str__(self):
        return self.country_code + "\t" + str(len(self.day_list)) + "\t" + str(self.cases_sum) + "\t" \
               + str(self.deaths_sum)

    def __lt__(self, other):
        return self.cases_sum < other.cases_sum

    def __gt__(self, other):
        return self.cases_sum > other.cases_sum

    def __eq__(self, other):
        return self.cases_sum == other.cases_sum


if __name__ == '__main__':
    ob1 = Przypadki_kraj("PL")
    ob1.add_day_data("23.04.2020", 56, 3, )
    ob1.add_day_data("23.04.2020", 50000, 200)
    ob1.add_day_data("25.04.2020", 100, 10)
    ob2 = Przypadki_kraj.object_from_line(
        "04.08.2020	4	8	2020	37	4	Afghanistan	AF	AFG	38041757	Asia	2,97567749")
    ob3 = Przypadki_kraj.object_from_data("01.05.2019", 45, 1, "DE")
    print(ob1)
    print(ob2)
    print(ob3)
    print(ob1 == ob2)
    print(ob1 == ob1)
    print(ob2 > ob3)
    print(ob2 < ob3)
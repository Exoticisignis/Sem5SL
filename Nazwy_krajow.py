from L6Z1 import LevSim

class Nazwy_krajow:
    def __init__(self):
        self.country_dict = {}

    def in_dictionary(self, key):
        if key in self.country_dict:
            return True
        return False

    def add_country(self, country_code, country_name, continent):
        if self.in_dictionary(country_code):
            return False
        else:
            for temp_code, (temp_country, temp_continent) in self.country_dict.items():
                if LevSim(country_name, temp_country) < 2:
                    return False

            self.country_dict[country_code] = (country_name, continent)
            return True

    def get_country_name_from_code(self, code):
        if code in self.country_dict:
            return self.country_dict[code][0]
        else:
            return None

    def get_country_code_from_name(self, country):
        temp_country_dict = {}
        act_level = 0
        while act_level < 5:
            for temp_code, (temp_country, temp_continent) in self.country_dict.items():
                levSim = LevSim(country, temp_country)
                if levSim <= act_level:
                    temp_country_dict[temp_country] = (str(levSim), temp_code)
            act_level += 1
        if len(temp_country_dict) == 1:
            return str(temp_country_dict.values())
        else:
            return 'Niejednoznaczność nazwy: %d kandydatów' % len(temp_country_dict)

    def __str__(self):
        return self.country_dict


if __name__ == '__main__':
    ob = Nazwy_krajow()
    ob.add_country('PL', 'Poland', 'Europe')
    ob.add_country('PL', 'Pola', 'Eur')
    ob.add_country('PT', 'Polan', 'Euro')
    ob.add_country('DE', 'Germany', 'Europe')
    ob.add_country('DP', 'Germluy', 'Europe')

    print(ob.get_country_name_from_code('PL'))
    print(ob.get_country_name_from_code('AU'))
    print(ob.get_country_code_from_name('Germ'))
    print(ob.get_country_code_from_name('Polan'))
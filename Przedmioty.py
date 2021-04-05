from L6Z1 import LevSim
class Przedmioty:
    def __init__(self):
        self.__subjectDict = {}

    def getCodeFromName(self, subName):
        if not self.__subjectDict:
            return None

        temp_list = []
        act_level = 0
        while act_level < 5:
            for code, name in self.__subjectDict.items():
                if LevSim(name, subName) <= act_level:
                    temp_list.append(code)
            act_level += 1
        returnList = list(set(temp_list))
        if len(returnList) > 1:
            return None
        return returnList[0]

    def addSubject(self, subCode, subName):
        if subCode in self.__subjectDict.keys() or subName in self.__subjectDict.values():
            return -1
        self.__subjectDict[subCode] = subName
        return len(self.__subjectDict.keys())

    def getSubject(self, subCode):
        if subCode in self.__subjectDict.keys():
            return self.__subjectDict[subCode]
        return None

    def __str__(self):
        return str(self.__subjectDict)

if __name__ == '__main__':
    p = Przedmioty()
    p.addSubject('Mat', 'Maths')
    p.addSubject('Ph', 'Physics')
    print(p.getCodeFromName('Maths'))

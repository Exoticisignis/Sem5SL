from Osoba import Osoba
from Pracownik import Pracownik
from Przedmioty import Przedmioty
from Student import Student

def getList():
    list = []
    p1 = Pracownik('Jan', 'Kowalski', '1985-03-09')
    p1.addPublication(2007, 30)
    p1.addPublication(2003, 40)
    p1.addPublication(2010, 70)
    p1.addPublication(2015, 80)
    list.append(p1)
    p2 = Pracownik('Kamil', 'Nowak','1974-12-07')
    p2.addPublication(2018, 80)
    p2.addPublication(1992, 30)
    p2.addPublication(2001, 60)
    p2.addPublication(2007, 40)
    p2.addPublication(1998, 80)
    p2.addPublication(2017, 80)
    list.append(p2)
    p3 = Pracownik('Bartosz', 'Pilsudski', '1982-06-05')
    p3.addPublication(2007, 80)
    p3.addPublication(2003, 30)
    p3.addPublication(2010, 60)
    list.append(p3)

    s1 = Student('Mr', 'X', '1999-09-07')
    s1.addMark('FIZ', '5.0')
    s1.addMark('ANG', '4.5')
    list.append(s1)
    s2 = Student('May', 'Be', '1997-11-07')
    s2.addMark('BIO', '2.0')
    s2.addMark('BIO', '3.0')
    s2.addMark('ANG', '4.5')
    list.append(s2)
    s3 = Student('For', 'Azeroth', '1998-11-18')
    s3.addMark('BIO', '5.0')
    s3.addMark('MT', '3.5')
    list.append(s3)
    s4 = Student('Pablo', 'Eskobar', '2000-05-02')
    s4.addMark('ANG', '5.5')
    s4.addMark('MT', '2.5')
    list.append(s4)
    s5 = Student('Looney', 'Tune', '2001-06-24')
    s5.addMark('BIO', '4.5')
    s5.addMark('FIZ', '5.5')
    list.append(s5)
    s6 = Student('Disney', 'World', '1999-11-07')
    s6.addMark('PL', '5.0')
    s6.addMark('FIZ', '3.0')
    s6.addMark('ANG', '4.5')
    list.append(s6)
    s7 = Student('The', 'Mandolorian', '2000-01-27')
    s7.addMark('MT', '4.5')
    s7.addMark('FIZ', '4.0')
    s7.addMark('ANG', '4.5')
    list.append(s7)
    s8 = Student('Mark', 'Reed', '1999-06-24')
    s8.addMark('BIO', '4.5')
    s8.addMark('FIZ', '3.5')
    list.append(s8)
    s9 = Student('Han', 'Solo', '1999-06-24')
    s9.addMark('PL', '4.5')
    s9.addMark('ANG', '3.5')
    list.append(s9)
    s10 = Student('Chewing', 'Gum', '2001-08-14')
    s10.addMark('PL', '4.5')
    s10.addMark('ANG', '3.5')
    list.append(s10)
    return list

def getSubjects():
    sub = Przedmioty()
    sub.addSubject('MT', 'Matematyka')
    sub.addSubject('FIZ', 'Fizyka')
    sub.addSubject('ANG', 'Angielski')
    sub.addSubject('PL', 'Polski')
    sub.addSubject('BIO', 'Biologia')
    return sub

def employeRangeList(min, max, persons):
    if min < max:
        pracownicy = []
        for person in persons:
            if isinstance(person, Pracownik):
                if min <= person.getAge() <= max:
                    pracownicy.append(person)
        return pracownicy
    else :
        return []

def bestWorkers(persons):
    best = []
    max = 0
    for person in persons:
        if person.pointsFor4Years() > max:
            max = person.pointsFor4Years()
    for person in persons:
        if person.pointsFor4Years() == max:
            best.append(person)
    print ('Best worker(s) for last 4 years:')
    for person in best:
        print(person.getSurname() + ', points: ' + str(max))
    print()

def alphabetStud(list):
    students = []
    for person in list:
        if isinstance(person, Student):
            students.append(person)
    students.sort(key=lambda student: student.getSurname())
    print('Students sorted my surname:')
    for s in students:
        print(str(s))
    print()

def alphabetWork(list):
    workers = []
    for person in list:
        if isinstance(person, Pracownik):
            workers.append(person)
    workers.sort(key=lambda pracownik: pracownik.getSurname())
    print('Employees sorted my surname:')
    for w in workers:
        print(str(w))
    print()

def studentsMarks(list):
    students = []
    for person in list:
        if isinstance(person, Student):
            students.append(person)
    students.sort(key=lambda student: student.getAverage(), reverse=True)
    print('Students sorted my average:')
    for s in students:
        print(str(s) + ', Average: ' + str(s.getAverage()))
    print()

if __name__ == '__main__':
    list = getList()
    pracownicy = employeRangeList(40, 50, list)
    bestWorkers(pracownicy)
    alphabetStud(list)
    alphabetWork(list)
    studentsMarks(list)




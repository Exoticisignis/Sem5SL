from Znaczniki import Znaczniki
from Etykieta import Etykieta
from ZnacznikoweDane import ZnacznikowaneDane

if __name__ == '__main__':
    print('Znaczniki:')
    z1 = Znaczniki()
    z1.addString('sadafagf')
    #z1.addString('_ap_sfpijfs_')
    #z1.addString('z')
    z1.addString('prpwoms123')
    z1.addString('sad')
    z1.save('znaczniki.txt')
    print('Saved z1: ' + str(z1))
    z2 = Znaczniki()
    z2.open('znaczniki.txt')
    print('Readed z2: ' + str(z2))
    z3 = Znaczniki()
    z3.addString('asdk')
    z3.addString('sad')
    print('z3: ' + str(z3))
    print('Accepted for z1 from z3 : '+str(z1.getAccepted(z3)))
    print('Rejected for z1 from z3 : ' + str(z1.getRejected(z3)))
    print('Get string for distance for z1 and [sa]: ' +str(z1.getString('sa', 2)))
    print()
    print('Etykiety:')
    ciag1 = [ 'abc_', 'abcd_', '_abcde', '324']
    ciag2 = ['__abc', 'abc_', 'abcd_', '_abcde']
    ciag3 = ['__abc', 'abc_', 'abcd_', '_abcde']
    ciag4 = [ 'abc_', 'abcd_']
    ciag5 = ['123','345','678']
    e1 = Etykieta(ciag1)
    e2 = Etykieta(ciag2)
    e3 = Etykieta(ciag3)
    e4 = Etykieta(ciag4)
    e5 = Etykieta(ciag5)
    print('e1 :'+str(e1))
    print('e2 :'+str(e2))
    print('e3 :'+str(e3))
    print('e4 :'+str(e4))
    print('e5 :'+str(e5))
    print('e4 + e5: ' +str(e4+e5))
    print('e2 == e1: ' +str(e2 == e1))
    print('e2 == e3: '+str(e2 == e3))
    print('e1 * e2: '+str(e1 * e2))
    print('e1 - e2: '+str(e1 - e2))
    print('e4 <= e1: '+str(e4 <= e1))
    print('e1 >= e4: '+str(e1 >= e4))
    print('e4 != e5: ' +str(e4 != e5))




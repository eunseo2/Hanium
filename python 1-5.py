#10.1
##class Thing:
##    pass
##
##example = Thing() #객체 생성
##
##print(Thing)
##print(example)



10.2 #클래스 속성
class Thing2:
    letters = 'abc'
print(Thing2.letters)
a = Thing2()
print(a.letters)

#10.3 객체 속성

class Thing3:
    def __init__(self): #객체를 생성할 때 속성을 할당 
        self.letters ='xyz'
        
#print(Thing3.letters) 


something= Thing3() #객체 생성 
print(something.letters)














#10.4
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol=symbol
        self.number= number
hydrogen = Element('Hydrogen','H',1)


#10.5
el_dict ={'name':'Hydrogen','symbol':'H','number':1 }
hydrogen = Element(el_dict['name'],el_dict['symbol'],el_dict['number'])




#10.6
el_dict ={'name':'Hydrogen','symbol':'H','number':1 }
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol=symbol
        self.number= number
    def dump(self):
        print(f'name:{self.name}, symbol:{self.symbol}, number:{self.number} ')
   
hydrogen = Element(**el_dict) #**el_dict는 키워드 인수 방법 1
#hydrogen= Element(name = 'Hydrogen' , symbol = 'H', number =1) #방법2 
hydrogen.dump()
print("-------------------------------------")


#10.7
print(hydrogen)
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol=symbol
        self.number= number
    def __str__(self):
        return f'name:{self.name}, symbol:{self.symbol}, number:{self.number} '

hydrogen = Element(**el_dict)
print(hydrogen)



#10.8
###getter 매서드 앞에는  @property 데커레이터를 쓴다.
##
##class Element:
##    def __init__(self,name,symbol,number):
##        self.__name = name
##        self.__symbol=symbol
##        self.__number= number
##    @property
##    def name(self):
##        return self.__name
##    @property
##    def symbol(self):
##        return self.__symbol
##    @property
##    def number(self):
##        return self.__number
##
##hydrogen = Element('hydrogen','H',1)
##
###hydrogen.name = 'hy' error남
##print(f'name:{hydrogen.name}, symbol:{hydrogen.symbol}, number:{hydrogen.number} ')
##

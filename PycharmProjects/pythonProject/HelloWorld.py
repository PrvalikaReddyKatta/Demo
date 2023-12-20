print('Hello')

b, c, d, e = 'vinay', 3.5, 5, True
print('Value of c', d)
print(type(e))

list = [1, 2, 3, 6, 8, 9]
print(list[-1:3])
list.append('hello')
del list[0]
print(list)

dic = {1: 'Hi', 'surya' : 'Palli', 2 : 123 }
print(dic[1])

print('#######While loop#######')
k = 6
while k>1:
    if k == 3:
        k = k - 1
        continue
    print(k)
    k = k - 1

print('######  FUnctions ######')

def FunctionKey(a, b):
    print('functions', a+b)

FunctionKey(2, 5)


print('###OOPS')
class Selenium:
    num = 50
    def __init__(self,a,b):
        self.First = a
        self.Second = b
        print('selenium with python 1')
    def getData(self):
         print('selenium with python')
    def Summation(self):
        return self.First +  self.Second + self.num

obj = Selenium(1,2)
obj.getData()
print(obj.Summation())

##String and functions in Python
str = 'Pravalika'

print(str[1])

Name = 'PravalikaKatta'
var = Name.split('a')
print(var[3])



class Person :
    def __init__(self,name = "dachangjing", age = 38):
        self.name = name
        self.age = age


p1 = Person(name = "zhuyuanzhang")
p2 = Person(age = 55)


print(p1.name,p1.age)
print(p2.name,p2.age)
del p2.age
print(p1.name,p1.age)
#print(p2.name,p2.age)

p3 = Person(age = 33)
print(p3.name,p3.age)
p3.addinod = "test for add"
print(p3.addinod)

#cant del class
#del Person.name
#print(p1.name,p1.age)
#print(p2.name,p2.age)

# @classmethod 方法
'''
classmethod 属于类，类调用以及实例调用都会自动绑定
'''
class Tiger :
#用@classmethod修饰 ，需传参cls
    @classmethod
    def info(cls):
        print('Tiger inof')

Tiger.info()

#@staticmethod
'''
staticmethod 相当于函数，类调用以及实例调用都不会自动绑定
'''
class Tiger1 :
    @staticmethod
    def info(p):
        print("Tiger1 info")
        print(p)

Tiger1.info(24)

#装饰器
'''
装饰器本质是一个函数
1 被装饰的函数作为参数传入装饰器
2 被装饰的函数被装饰器函数的返回值替换
'''
#注意，装饰器函数必须有传参
def func (fn):
    print("func 函数")
    print(fn)
    return 'abcdefg'

@func
def bar():
    print('bar 函数')

print(bar)
#bar()无法被调用，已经被替换为 abcdefg
#bar()

#属性
#property 使用 合成实例变量（或属性）,注意合成的是变量
#property(fget=none,fset=none,fdel=none,doc=none)

class proper_test:
    def __init__(self,width,hight):
        self.width = width
        self.hight = hight
    def getarea(self):
        print('getarea')
        return self.width * self.hight
    def getproper(self):
        print(self.width,self.hight)
    def setproper(self,proper):
        print('setproper')
        self.width = proper[0]
        self.hight = proper[1]
    area = property(fget = getarea )

    proper = property(fget = getproper,fset = setproper)

prope1 = proper_test(30,50)

print(prope1.area)
print(prope1.proper)

prope1.proper = (40,60)

print(prope1.area)
print(prope1.proper)

#property 装饰器
class proper_test2:
    def __init__(self,width,hight):
        self.width = width
        self.hight = hight
    @property
    def area(self):
        print('area')
        return self.width * self.hight
    @property
    def proper(self):
        print(self.width,self.hight)
    @proper.setter
    def proper(self,proper):
        print('setproper')
        self.width = proper[0]
        self.hight = proper[1]


prope2 = proper_test2(30,50)

print(prope2.area)
print(prope2.proper)

prope1.proper = (40,60)

print(prope1.area)
print(prope1.proper)
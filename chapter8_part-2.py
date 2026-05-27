#chapter-9 (oops)- [Part-2]
#del keyword
# class student:
#     def __init__(self,name):
#         self.name = name

# s1 = student("anam")
# print(s1.name)
# del s1.name
# print(s1.name)

#private(like) attributes and methods
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #when we used underscore before so it means its private attribute
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())

# class Person:
#     __name = "Anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#      self.__hello()


# p1 = Person()
# print(p1.welcome())

#inheritance - features in you by your parent class
#single inheritance


# class car:
#     @staticmethod
#     def start():
#         print("car started..")

#     def stop():
#         print("car stopped..")

# class ToyotaCar(car):
#     def __init__(self,brand):
#         self.brand = brand

# Car1 = ToyotaCar("fortuner")
# Car2 = ToyotaCar("prius")
# print(Car1.brand)

#types of inheritance
#multi-level inheritance
# class fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type
# car3 = fortuner("diesal")
# car3.start()

#multiple inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"
C1 = C()
print(C1.varC,"\n",C1.varA,"\n",C1.varB)

#super method 
class car:

    def __init__(self,type):
       self.type = type

    @staticmethod #these are those methods when we dont wanna access or modify the classstate
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(car):
    def __init__(self,name,type):
      super().__init__(type)
      self.name = name
      super().start()

Car1 = ToyotaCar("prius","electric")

print(Car1.type)

#classmethod- those methods which access the attribute of the class and change the class attributes 
class Person:
     name = "anonymous"

     #def changeName(self,name):
      #self.__class__.name = "rahul"
      #self.__class__. Person.
     @classmethod
     def changeName(cls,name):
         cls.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)


#property method- to use method as the property 
#method 1

class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
      

    # def calcPercentage(self):
    #    self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
    @property #easy mthod 2
    def percentage(self):
       return str((self.phy + self.chem + self.math)/3) + "%"


stu1 = student(98,94,98)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)

#polymorphism - same operator have allowed to have diffrent meaning according to the contex
#becoz of diffrent dtype have the diffrent meanig called operator overloading
print(1 + 2) #3
print(type(1))
print(type("apna"))
print("apna"+"college")#concatenate #apnacollege
print([1,2,3]+[4,5,6]) #merge

print(type([1,2,3]))

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)
    
    def __mul__(self,num2):
        newReal = self.real * num2.real
        newImg = self.img * num2.img
        return complex(newReal,newImg)
    
num1 = complex(1,3)
num1.showNumber()

num2 = complex(4,6)
num2.showNumber()

num3 = num1 * num2
num3.showNumber()

#practice question 1'

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * (22/7) * 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#practice question 2
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary 

    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","it","75000")

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()

#practice question 3
class Order:
    def __init__(self,item,prize):
        self.item = item 
        self.prize = prize

    def __gt__(self,odr2):
        return self.prize > odr2.prize
    

odr1 = Order("Chips", 30)
odr2 = Order("tea", 20)

print(odr1 > odr2) #true


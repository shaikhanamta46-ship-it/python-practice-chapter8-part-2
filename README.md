#  Python OOPS (Part-2)

> Complete notes and practice of Object Oriented Programming in Python.

---

##  Topics Covered

- `del` Keyword
- Private Attributes & Methods
- Inheritance
  - Single Inheritance
  - Multiple Inheritance
- `super()` Method
- `@classmethod`
- `@property`
- Polymorphism
- Operator Overloading
- Practice Questions

---

#  `del` Keyword

Used to delete object properties or objects.

## Example

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("anam")

print(s1.name)

del s1.name
```

---

#  Private Attributes & Methods

Private members are created using `__`.

## Example

```python
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
acc1.reset_pass()
```

---

#  Inheritance

Inheritance allows child classes to use properties and methods of parent classes.

---

##  Single Inheritance

```python
class Car:
    def start(self):
        print("Car Started")

class ToyotaCar(Car):
    pass
```

---

##  Multiple Inheritance

```python
class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

class C(A, B):
    varC = "Welcome to Class C"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)
```

---

#  `super()` Method

Used to access parent class constructor and methods.

## Example

```python
class Car:

    def __init__(self, type):
        self.type = type

class ToyotaCar(Car):

    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("Prius", "Electric")

print(car1.type)
```

---

#  `@classmethod`

Used to modify class attributes.

## Example

```python
class Person:

    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()

p1.changeName("Rahul")

print(Person.name)
```

---

#  `@property`

Converts methods into properties.

## Example

```python
class Student:

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 94, 98)

print(stu1.percentage)
```

---

#  Polymorphism

Same operator behaves differently for different data types.

## Example

```python
print(1 + 2)

print("Apna" + "College")

print([1, 2, 3] + [4, 5, 6])
```

---

#  Operator Overloading

## Complex Number Example

```python
class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, num2):
        return Complex(
            self.real + num2.real,
            self.img + num2.img
        )
```

---

#  Practice Questions

---

## 1️ Circle Class

```python
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
```

---

## 2️ Employee & Engineer

```python
class Employee:

    def showDetails(self):
        print("Employee Details")

class Engineer(Employee):
    pass
```

---

## 3️ Comparing Orders using `>`

```python
class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
```

---

#  Concepts Learned

- Encapsulation
- Inheritance
- Polymorphism
- Operator Overloading
- Class Methods
- Property Decorators

---

# Tech Used

- Python
- OOP Concepts

---

#  Author
Anamta Shaikh

"""
My class
"""
import datetime


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


my_object = MyClass()


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"{self.owner} has EUR {self.balance}")


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def say_hello(self):
        print(f"{self.name} says hello")


p1 = Person("John", 42)
print(p1.name)
print(p1.age)

p2 = Person("Jane", 42)
p2.say_hello()


class Student(Person):
    def learn(self, language):
        print(f"{self.name} is learning {language}")


s1 = Student('John', 42)
s1.say_hello()
s1.learn('java')

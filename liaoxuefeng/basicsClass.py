#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 # 基础 类 对象

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_score(self):
        print('name : %s age : %d' % (self.name, self.age))
    def get_name(self):
        return self.name

bart = Student('whchao', 18)
bart.print_score()
print(bart.get_name())

 # 继承对象
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

dog = Dog()
dog.run()

print(isinstance(dog, Student))  # FALSE
print(isinstance(dog, Animal))   # Ture

def run_twice(animal):
    animal.run()

run_twice(Dog())
run_twice(Animal())

print(type(123))
print(type(Animal()))
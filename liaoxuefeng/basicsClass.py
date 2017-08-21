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

# run_twice(Dog())
# run_twice(Animal())

# print(type(123))   # <class 'int'>
# print(type(Animal())) # <class '__main__.Animal'>


# print(bart)


class StudentTwo(object):

    # def __init__(self, _score):
    #     self._score = _score

    # def get_score(self):
    @property
    def score(self):
        return self._score

    # def set_score(self, value):
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            return ValueError('socre must be an integer!')
        if value < 0 or value > 100:
            return ValueError('score must between 0 ~ 100')
        self._score = value

s = StudentTwo()
s.score = 40
print(s.score)
# print('00')
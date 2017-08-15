# coding: utf-8

import math

import mycompany.hello

classmates = ('Michael', 'Bob', 'Tracy')

# print(len(classmates))

t = (1, 2)
# print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# print(L[0])

age = 9
if age >= 10:
    print (age)
else:
        print ('no', age)

# birth = int(input('birth: '))
# if birth >= 2000:
#     print(birth)
# else:
#     print('no', birth)


##  循环
sum = 0
for name in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += name
print(sum)

sumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum1 = (sumList[0] + sumList[len(sumList) - 1]) * len(sumList) / 2   ## 数列求和公式

print(sum1)

## continue
n = 0
while n < 10:
    n = n + 1
    if (n % 2 == 0):
        continue
print(n)


## dict(Map) && set

d = {'Michael': 95, "Olio" : 899}
print(d.get('Olio'))

s = set([1, 1, 2, 2, 3, 3])
print(s)

## 函数
print(abs(2))

print(hex(99))

# def my_abs(x):
#     if x > 0:
#         return x
#     else:
#         return abs(x)
#
# print(my_abs('A'))

def add_end(L = []):
    L.append('END')
    return L

print(add_end(['A', "B"]))

print(add_end())
print(add_end())


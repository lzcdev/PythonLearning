#!/usr/bin/python
#coding:utf-8

class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(student: %s, %s, %s)' % (self.name, self.gender, self.score)
    # __repr__ == __str__


s = Student('Bob', 'male', 88)
print s
# s


# 根据num计算出斐波那契数列的前N个元素。
class Fib(object):

    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L
        
    def __str__(self):
        return str(self.numbers)
    
    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.__score >= 80:
            return 'A'
        elif self.__score < 60:
            return 'C'
        else:
            return 'B'

s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade



# 简化版 斐波那契数列
class Fib(object):

    def __call__(self, num):
        a, b, l = 0, 1, []
        for n in range(num):
            l.append(a)
            a, b = b, a + b
        return l

f = Fib()
print f(10)




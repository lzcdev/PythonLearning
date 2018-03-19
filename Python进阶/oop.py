#!/usr/bin/python
#coding: utf-8

# class Person(object):
# 	pass
# xiaoming = Person()	
# xiaohong = Person()
# print xiaoming
# print xiaohong
# print xiaoming == xiaohong
		
class Person(object):
			"""docstring for Person"""
			count = 0
			def __init__(self, name, gender, birth, **kw):
				super(Person, self).__init__()
				Person.count = Person.count + 1
				self.name = name
				self.gender = gender
				self.birth = birth
				for k, v in kw.iteritems():
					setattr(self,k,v)

xiaoming = Person('Xiaoming', 'male', '1992', job='teacher')
print xiaoming
print xiaoming.gender
print xiaoming.job
print xiaoming.count

class Person(object):

    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()       
						
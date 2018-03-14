#!/usr/bin/python
#coding: utf-8

import math

# 高阶函数：函数可作为参数
def add(x, y, f):
	return f(x) + f(y)
print add(-5, 9, abs)
print add(9, 25, math.sqrt)



# map()函数
def format_name(s):
		# return s[0].upper() + s[1:].lower()
		return s.capitalize()
print map(format_name, ['adam', 'LISA', 'barT'])


# reduce()函数
def prod(x, y):
	return x * y
print reduce(prod, [2, 4, 5, 7, 12])


# filter()函数,利用filter()过滤出1~100中平方根是整数的数
def is_sqr(x):
	return math.sqrt(x) == (int)(math.sqrt(x))
print filter(is_sqr, range(1, 101))


# 忽略大小写排序的算法
def cmp_ignore_case(s1, s2):
	if s1.lower() < s2.lower():
		return -1
	if s1.lower() > s2.lower():
		return 1
	return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)		


# 一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积
def calc_prod(lst):
	def lazy_prod():
		def prod(x, y):
			return x * y
		return reduce(prod, lst)
	return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()


# 匿名函数
print filter(lambda s : s and s.strip() > 0, ['test', None, '', 'str', ' ', 'end'])



# 装饰器,decorate本质上是一个高阶函数，它接收一个函数作为参数，然后返回一个新函数
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
# f = factorial(f)
@log
def factorial(n):
	return reduce(lambda x, y: x*y, range(1, n + 1))
print factorial(10)


# 计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。
import time

def performance(f):
	def fn(*args, **kw):
		t1 = time.time()
		r = f(*args, **kw)
		t2 = time.time()
		print 'call %s() in %fs' % (f.__name__, (t2 - t1))
		return r
	return fn
@performance
def factorial1(n):
	return reduce(lambda x,y : x * y, range(1, n + 1))
print factorial1(10)	



import functools
def log(f):
	@functools.wraps(f)
	def wrapper(*args, **kw):
		print 'call...'
		return f(*args, **kw)
	return wrapper	


# 偏函数
sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])	






































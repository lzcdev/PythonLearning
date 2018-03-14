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

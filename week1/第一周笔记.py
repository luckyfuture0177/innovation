#!/usr/bin/env python
#list python内置的数据类型 是列表：list
#list是一种有序的集合 可以随时修改
classmates = ['zhao','qian','sun']
print(classmates)
lens = len(classmates)
print(lens)
#用len（）获得list元素个数
print(classmates[0])
#用索引来访问元素的位置
print(classmates[-1])
#用-1做索引 直接获得最后一个元素
classmates.append('Adam') #加到末尾
classmates.insert(1,'jack') #加到指定位置
classmates.pop(1)#删除

classmates1 = ('li','zhou','wu')
#tuple 初始化后不能修改












# if given a list or tuple,we can use for to traversing it
# we call it Lteration
'''python's for loop is more abstract than C's
because python's for loop can be used not only on list or tuples,
but also on other iterable objects.'''
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
# by defult dict's lterate is key
#if you want value
for value in d.values():
    print(value)
# if you want key and value
for k,v in d.items():
    print(k,v)
# string is itrable
for ch in 'ABC':
    print(ch)
# judge an object as an iterable object
from collections import Iterable
print(isinstance('abs',Iterable))
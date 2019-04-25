'''默认参数的定义
默认参数必须指向不变的对象'''

def add_end(l=None):
    if l is None:
        l=[]
    l.append('end')
    return l
a=add_end()
b=add_end()
print(a,b)

'''可变参数'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n**2
    return sum
print(calc([1,2,3]))

def calcs(*numbers): # 把函数的参数变成可变参数
    sums = 0
    for n in numbers:
        sums = sums + n**2
    return sums
print(calcs(1,2,3)) # 可以传入任意个参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
nums = [1,2,3]
print(calcs(*nums))
# 在list前加* 把list的元素变成可变参数传进去、

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person( name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)
a=person('Akie',30)
print(a)
b=person('bob',30,city='beijing')
# 传入任意个关键字参数

# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)




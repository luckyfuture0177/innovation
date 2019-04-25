# 递归函数 recursive function
# 在内部调用自己本身 call itself on the inside
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
m = 0
a = fact(171)
print(a)
while a!=0:
    a=int(a / 10)
    m +=1
print(m)
'''使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）
这种数据结构实现的，每当进入一个函数调用，
栈就会加一层栈帧，每当函数返回，
栈就会减一层栈帧。由于栈的大小不是无限的，
所以，递归调用的次数过多，会导致栈溢出。'''

# 尾递归 无论多少次调用 都只占用一个栈 不会溢出
def facts(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(180))


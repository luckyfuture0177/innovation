print(abs(-177))
# abs函数求绝对值
print(help(abs))
print(max(1, 2, 3, 4, 5, 6, 5, 34, 34, 2))
print(hex(255))
# hex函数将十进制转换为十六进制

# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
# 对参数类型做检查
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-233))

#定义空函数
def nop():
    pass
#pass 作为占位符 让代码运行起来

import math
def move(x,y,step,angle = 0):
    nx = x+step * math.cos(angle)
    ny = y+step * math.sin(angle)
    return nx,ny

#返回多个值
print(move(100,100,60,math.pi/6))
#实际上返回的是一个tulpe

def quadratic(a,b,c):
    if b*b-4*a*c < 0:
        print('方程无解')
    else:
        x1 = ((-b)+math.sqrt(b*b-4*a*c))/a*2
        x2 = ((-b)-math.sqrt(b*b-4*a*c))/a*2
        return x1,x2
print(quadratic(1,-14,-8))
f1 = 0
f2 = 1
l=[]
for i in range(10):
    a=f1+f2
    f2=f1
    f1=a
    print(a, '\n')
    l.append(a)

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print(fib(10))
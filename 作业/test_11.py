
def rabbit(n):
    l = [1,1]
    if n == 1:
        return l[1]
    elif n==2:
        return l
    else:
        for i in range(3,n+1):
            l.append(l[-1]+l[-2])
        return l
print(rabbit(2))











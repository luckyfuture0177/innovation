def paixu (x, y, z):
    if x > y:
        (x, y) = (y, x)
    elif x > z:
        (x,z) = (z,x)
    elif y>z:
        (y,z)=(z,y)
    return x,y,z
print(paixu(4,2,8))
l = []
for i in range(0,3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)
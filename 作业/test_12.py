import math
sum = 0

for i in range(101,201):
    k=1
    for j in range(2,int(math.sqrt(i))+1):
        if (i % j == 0):
            k=0
            break
    if k==1:
        sum=1+sum
        print(i)
print('素数共有：',sum,'个')


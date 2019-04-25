l=[]
sum = 0
for i in range(2,1001):
    for j in range(1,i):
        if i%j==0:
            l.append(j)
    for k in l:
        sum +=k
    if sum==i:
        print(i)
    sum=0
    l=[]

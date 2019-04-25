for i in range(1,1000):
    sum=0
    k=i
    while i!=0:
        j=i%10
        sum = j*j*j+sum
        i=int(i/10)
    if sum==k:
        print(k)





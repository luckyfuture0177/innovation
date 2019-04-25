for i in range(-10000,10000):
    sum = i+100
    for j in range(1,1000):
        if(sum==j*j):
            sum=sum+168
            for k in range(1,1000):
                if(sum==k*k):

                    print(sum-268)
                    break
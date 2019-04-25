def reducenum(n):
    for i in range(2,int(n+1)):
        if n % i ==0:
            n = n/i
            if n==1:
                print(i)
            else:
                print(i)
                print(reducenum(n))
            break
reducenum(90)


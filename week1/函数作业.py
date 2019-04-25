def product(*number):
    sum = 1
    for n in number:
        sum=sum*n
    return sum
l=[1,2,3]
print(product(*l))

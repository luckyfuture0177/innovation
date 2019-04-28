'''求1+2!+3!+...+20!的和'''
s=1
s1=0
for n in range(1,21):
    s = 1
    while n != 0:
        s *= n
        n -= 1
    s1 += s
print(s1)
age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
elif age>=6: #elif 做更细致的判断
    print('your age is',age)
    print('teenager')
else:
    print('your age is',age)
    print('kid')
s = input('birth:')
birth = int(s) #input 返回数据类型是str
if birth < 2000:
    print('00前')
else:
    print('00后')
def trim(s):
    i = 0
    j = -1
    while s[i] == ' ':
        i = i+1
    while s[j:] == ' ':
        j = j-1
    if j == -1:
        s = s[i:]
    else:
        s = s[i:j]
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
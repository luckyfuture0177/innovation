'''Use iteration to find the minimum and maximum values ​​in a list and return a tuple'''
def findMinAndMax(l):
    if len(l)<1:
        j = None
        h = None
    else:
        j = l[0]
        h = l[0]
        for i in l:
            if i>=j:
                j=i
            if i<=h:
                h=i
    print(j,h)
    return (h,j)
# test
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
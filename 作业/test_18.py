'''题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。'''
def successiveplus(i,j):
    sum = 0
    k=i
    while j!=0:
        sum += i
        j -= 1
        print(i)
        i = i*10+k
    return sum
print(successiveplus(4,4))






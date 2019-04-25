'''题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''
def rebound(hight ,time):
    sum = -100
    while time > 0:
        sum += hight * 2
        hight = hight/2
        time -= 1
    return hight,sum
print(rebound(100,10))

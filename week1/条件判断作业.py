hight = 1.65
wight = 65
bmi = (wight/(hight*hight))
print('BMI:',bmi)
if bmi >= 32:
    print('very fat')
elif bmi >= 28:
    print('fat')
elif bmi >= 25:
    print('overwight')
elif bmi >= 18.5:
    print('normal')
else:
    print('light')

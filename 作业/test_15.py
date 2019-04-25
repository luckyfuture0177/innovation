score = int(input('please type your score'))
if score >= 90:
    grade= 'A'
elif score >=60 and score<90:
    grade= 'B'
else:
    grade='C'
print(grade)

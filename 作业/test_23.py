'''output a diamond with"*"   '''
for i in range(1,5):
    j= (7-(2*i-1))/2
    while j !=0:
        print(' ',end='')
        j -= 1
    j = 2*i-1
    while j != 0:
        print('*',end='')
        j -= 1
    print('')
for q in range(3,0,-1):
    j = (7 - (2 * q - 1)) / 2
    while j != 0:
        print(' ',end='')
        j -= 1
    j = 2 * q - 1
    while j != 0:
        print('*',end='')    # avoid Automatic line break
        j -= 1
    print('')



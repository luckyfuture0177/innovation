year = int(input('year:'))
month = input('month:')
day = int(input('day:'))
month_dict={'0':0,'1':31,'3':31,'5':31,'7':31,'8':31,'10':31,'12':31,'4':30,'6':30,'9':30,'11':30,'2':28}
sum = 0
if ((year%4==0 and year%100!=0) or year%400==0):
    for i in range(0,int(month)-1):
        sum = sum+month_dict[month]
    if (int(month) > 2):
        print(sum+day+1)
    else:
        print(sum+day)
else:
    for i in range(0,int(month)-1):
        sum = sum+month_dict[month]
    print(sum + day)
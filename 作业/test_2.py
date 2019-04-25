i = int(input('Profit：'))
arr = [0,100000,200000,400000,600000,1000000]
rat = [0.1,0.075,0.05,0.03,0.015,0.01]
for x in range(0,6):
    if (i >= arr[5-x]):
        i = i+(i-arr[5-x])*rat[5-x]
        break
print(i)
sum = 0
for i in range(2, 10, 2):
    if(i % 2 ==0):
        sum = sum + i
        print('sum: {sum}'.format(sum=sum))
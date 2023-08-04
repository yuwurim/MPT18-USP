num = int(input())
mini = int(input())
maxi = int(input())

print('Tabuada do', num, 'de', mini, 'até', maxi)
for x in range(mini,maxi+1):
    print(num,"x",x,"=",num*x)
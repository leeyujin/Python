import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for i in a :
    if(i==1) :
        cnt +=1
        sum +=cnt
    else :
        cnt = 0


'''
b= [0]*n

for i in range(0,n) :

    if ( i == 0 ) :
        b[i] = a[i]
        continue

    if( a[i-1] == 1) :
        if(a[i] == 1 ):
            b[i] += b[i-1] + 1
    elif( a[i-1] == 0 ) :
        if( a[i] == 1 ) :
            b[i] = 1
    else:
        b[i]=0


sum = 0
for j in range(n) :
    sum += b[j]
'''
print(sum)
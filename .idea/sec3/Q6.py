#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
# a = [ [0]*5 for _ in range(5) ]

a = [ list( map(int, input().split())) for _ in range(n) ]

'''
a = list()
for _ in range(n) :
    a.append( list(map(int,input().split())) )
'''

b = list()

# 행의 합
for i in range(n) :
    sum=0
    for j in range (n) :
        sum += a[i][j]
    b.append(sum)

# 열의 합
for i in range(n) :
    sum=0
    for j in range (n) :
        sum += a[j][i]
    b.append(sum)

# 우측 대각선의 합
sum=0
for i in range(n) :
    sum += a[i][i]
b.append(sum)

# 좌측 대각선의 합
sum = 0
for i in range(n) :
    sum += a[n-i-1][n-i-1]
b.append(sum)

print(max(b))
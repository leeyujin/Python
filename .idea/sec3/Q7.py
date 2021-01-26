import sys
sys.stdin = open("input.txt","rt")
n = int(input())
a = [ list(map(int, input().split())) for _ in range(n)]

# 가운데 : center n/2  = 2
# 2-1, 2+1


center = int( n/2 )
sum = 0
s=e=center
for i in range(n) :
    for j in range(s,e+1) :
       sum += a[i][j]
    if ( i < center) :
        s -= 1
        e += 1
    else :
        s += 1
        e -= 1

print(sum)
'''
b = list()

for i in range(0,center+1):
    for j in range(i,n-i):
        if(i == 0 ):
            b.append( a[j][center] )
        else :
            b.append( a[j][center-i] )
            b.append( a[j][center+i] )

# print(b)
print(sum(b))

'''
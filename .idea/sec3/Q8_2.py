#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
a = [ list(map(int, input().split())) for _ in range (n)]

m = int(input())

for i in range(m) :
    rowNum, leftOrRigth, count = map(int, input().split())

    # 왼쪽
    if leftOrRigth == 0 :

        for j in range(count) :
            item = a[rowNum-1].pop(0)
            a[rowNum-1].append(item)

    #오른쪽
    else :
        for j in range(count) :
            item = a[rowNum-1].pop(n-1)
            a[rowNum-1].insert(0,item)

s,e,sum = 0,n,0
for i in range(n) :
    for j in range(s,e) :
        sum += a[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else:
        s -=1
        e += 1

print(sum)
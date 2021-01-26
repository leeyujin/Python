# import sys
# sys.stdin = open("input.txt","rt")

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(input())
a = [ list(map(int,input().split())) for _ in range(n) ]

a.insert(0, [0]*n)
a.append([0]*n)

for item in a :
    item.append(0)
    item.insert(0,0)

count = 0
# tmp = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
            if all( a[i][j] > a[ i+dx[k] ][ j+dy[k] ] for k in range(4) ) :
                count += 1

print(count)
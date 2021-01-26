#import sys
#sys.stdin = open("input.txt", "rt")

a = [ list(map(int,input().split())) for _ in range(9) ]
isTrue = True

# 행 검사
for i in a :
    b= [0] * 9
    for j in range(9) :
        idx = i[j] -1
        b[idx] += 1
        if ( b[idx] > 1) :
            isTrue = False

# 열 검사
for i in range(9) :
    b = [0] * 9
    for j in range(9) :
        idx = a[j][i] -1
        b[idx] += 1
        if ( b[idx] > 1) :
            isTrue = False

# 3*3 검사
# 0,3,6
dx = [0,1,2,0,1,2,0,1,2]
dy = [0,0,0,1,1,1,2,2,2]

for i in range(3) :
    for j in range(3) :
        b = [ 0 ] * 9
        x , y = i * 3, j  * 3
        for k in range(9) :
            idx =a[x + dx[k] ][y + dy[k] ]  -1
            b[idx] += 1
            if (b[idx] > 1) :
                isTrue=False
                break
if(isTrue) :
    print("YES")
else :
    print("NO")

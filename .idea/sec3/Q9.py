#import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = [ list(map(int, input().split())) for _ in range(n) ]

num = 0
for i in range(n) :
    for j in range(n) :
        val = a[i][j]

        left , up, right, down = 0, 0, 0, 0

        if  j-1 >= 0 :
            left = a[i][j-1]

        if j+1 < n :
            right = a[i][j+1]

        if i-1 >= 0 :
            up = a[i-1][j]

        if i+1 < n :
            down = a[i+1][j]

        if val > left and val > right and val > up and val > down :
            num +=1

print(num)

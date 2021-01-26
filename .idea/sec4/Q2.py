#import sys
#sys.stdin=open("input.txt","rt")

n,m = map(int,input().split())

a = list()

for _ in range(n) :
    a.append(int(input()))

maxVal = max(a)

start , end = 0, maxVal

res = list()

while start <= end :
    cnt = 0
    midLen = (start+end) //2

    for item in a :
        cnt +=  ( item // midLen )
    # 11 <= 18 - 길이 늘려야함
    if m <= cnt :
        res.append(midLen)
        start = midLen +1
    # 8개
    elif m > cnt :
        end = midLen -1

print(max(res))


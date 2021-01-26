#import sys
#sys.stdin = open("input.txt","rt")

n,c = map(int, input().split())

a = list()

for _ in range(n) :
    a.append(int(input()))

a.sort()

def countLen(interval) :
    last = len(a)
    cnt = 1
    i= 0
    j = i +1
    while(j <= last -1 ):
        if a[j] - a[i] >= interval :
            cnt += 1
            i = j
            j = i+1
        else :
            j += 1
    return cnt


lt= a[0]
rt = a[len(a)-1]
res = list()
while lt <= rt :
    mid = (lt+rt)//2
    cntLen = countLen(mid)

    if cntLen < c :
        rt = mid -1
    elif cntLen >= c :
        lt = mid + 1
        res.append(mid)

print(max(res))





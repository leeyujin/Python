import sys
sys.stdin=open("input.txt","rt")
n,m = map(int,input().split())

def countVal(val) :
    cnt = 1
    sum = 0
    for item in a :
        sum += item
        if(sum > val ) :
            cnt += 1
            sum = 0
            sum+=item
    return cnt


a = list(map(int, input().split()))

# 처음 생각 m개로 그루핑한 각 sum들 (15,13,17) / (10,11,19)의 최소값 비교 -> 최대값들 중 최소값

# 풀이 참조
lt , rt = 0, sum(a)
res = list()
while lt <= rt :
    mid = (lt+rt) //2
    num = countVal(mid)
    if num <= m  :
        res.append(mid)
        rt = mid -1
    elif num > m :
        lt = mid + 1

print(res)

print(min(res))
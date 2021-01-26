import sys
sys.stdin = open("input.txt","rt")

n = int(input())

a = list()

for _ in range(n) :
    key,weight = map(int,input().split())
    a.append( (key, weight) )

# key 순서로 sort
a.sort()

# 맨 마지막 녀석은 키가 제일 크니 카운트 +1
cnt = 0

length = len(a)
for i in range(length) :
    spec = a[i]
    weight = spec[1]

    # 나보다 키가 큰 얘들보다 몸무게가 많이 나가야함
    # isBigger = False
    # for j in range(i+1, length) :
    #     if (weight < a[j][1]) :
    #         isBigger = True
    #         break
    #
    # if( not isBigger ) :
    #     cnt+=1

    if all( weight > a[j][1] for j in range( i+1, length)  ) :
        print(spec)
        cnt += 1

print(cnt)
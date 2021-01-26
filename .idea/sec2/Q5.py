#import sys
#sys.stdin=open("input.txt","rt")
n,m = map(int, input().split())
# 이렇게 초기화하는것이 중요!
a = [0] * (n+m+1)

for i in range(1,n+1) :
    for j in range(1, m+1) :
        a[i+j] = a[i+j]+1

maxNum = max(a)

for index,value in enumerate(a) :
    if ( value == maxNum) :
        # 맨뒤에 " " 를 안붙이려면?
        print(index, end = " ")

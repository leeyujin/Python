import sys
sys.stdin=open("input.txt","rt")

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

''' 시간복잡도 nlogn -> 오른차순으로 정렬돼있는 두 리스트비교이므로 n시간으로 끝낼수있다
c=a+b
c.sort()
for i in c :
    print(i,end=" ")
'''
d=list()
lenA = len(a)
lenB = len(b)
#a len, b len 비교 -> idxA idxB 비교 -> 값 비교 후 idx ++
idxA = 0
idxB = 0

while lenA -1 >= idxA and lenB -1 >= idxB:
    
    if( a[idxA] <= b[idxB] ) :
        d.append(a[idxA])
        idxA += 1
    else :
        d.append(b[idxB])
        idxB += 1

    if(lenA == idxA) :
        #나머지 b 다 삽입
        d = d + b[idxB:]
    if(lenB == idxB) :
        #나머지 a 다 삽입
        d = d + a[idxA:]

for i in d :
    print(i, end=" ")
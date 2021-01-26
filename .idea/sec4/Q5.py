#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
inputList= list()
for _ in range(n) :
    a,b = map(int, input().split())
    inputList.append( (a,b) )

inputList.sort(key= lambda x : (x[1], x[0]))
cnt = 0
et = 0

for s,e in inputList:

    if( s >= et) :
        et = e
        cnt+=1

print(cnt)



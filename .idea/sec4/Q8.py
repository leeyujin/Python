#import sys
#sys.stdin = open("input.txt","rt")

n,m = map(int, input().split())
inputList = list(map(int,input().split()))

inputList.sort(reverse=True)

cnt = 0
boarded = [0] * n

for i in range(n) :

    sum = inputList[i]

    for j in range(i+1 , n) :
        if sum + inputList[j] <= m and boarded[j] == 0 and boarded[i] == 0 :
            boarded[j] = 1
            cnt += 1
            break
    boarded[i] = 1


print( n - cnt)



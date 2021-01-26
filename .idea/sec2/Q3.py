import sys
sys.stdin = open("input.txt","rt")
N,K = map(int, input().split())
inputList = list(map(int,input().split()))
sumSet = set()
for i in range(N) :
    for j in range(i+1, N):
        for m in range(j+1, N):
            sumSet.add(inputList[i] + inputList[j] + inputList[m])

sumSet=list(sumSet)
sumSet.sort(reverse=True)
print(sumSet[K-1])
import sys
sys.stdin = open("input.txt", "rt")

l = int(input())
inputList = list(map(int, input().split()))
m = int(input())

inputList.sort()

for _ in range(m) :
    inputList[0] += 1
    inputList[l-1] -= 1
    inputList.sort()

print(inputList[l-1] - inputList[0])


'''
for i in range(m) :
    maxVal = max(inputList)
    maxIdx = inputList.index(maxVal)
    minVal = min(inputList)
    minIdx = inputList.index(minVal)

    inputList.pop(maxIdx)
    inputList.insert(maxIdx, maxVal-1)

    inputList.pop(minIdx)
    inputList.insert(minIdx, minVal +1)


print( max(inputList) - min(inputList))

'''
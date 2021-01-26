import sys
sys.stdin = open("input.txt","rt")

n, m = map(int, input().split())
inputList = list(map(int, input().split()))

inputList.sort()

def getLeftLength(cutLength) :
    #자를 길이
    sumCutLength = 0

    for item in inputList :
        if item >= cutLength :
            sumCutLength += (item - cutLength)

    return sumCutLength



lt = 0
rt = inputList[len(inputList) - 1]
result = list()
while lt <= rt :
    mid = (lt + rt) // 2

    leftLength = getLeftLength(mid)
    if leftLength >= m :
        lt = mid + 1
        result.append(mid)
    elif leftLength < m :
        rt = mid - 1


print(max(result))



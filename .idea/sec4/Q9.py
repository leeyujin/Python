#import sys
from collections import deque
#sys.stdin=open("input.txt","rt")

n = int(input())
inputList = list(map(int, input().split()))
inputList = deque(inputList)


now = 0
res = list()


while inputList :
    left = inputList[0]
    right = inputList[-1]
    if now > left and now > right :
        break
    # now <= left or now <= right

    if left < right :
        # left < now < right
        if left < now :
            now = right
            inputList.pop()
            res.append("R")
        # now < left < right
        else :
            now = left
            inputList.popleft()
            res.append("L")
    else :
        # right< now < left
        if right < now :
            now = left
            inputList.popleft()
            res.append("L")
        # now < right < left
        else :
            now = right
            inputList.pop()
            res.append("R")


print(len(res))
for i in res :
    print(i, end="")


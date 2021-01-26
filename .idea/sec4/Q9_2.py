import sys
sys.stdin = open("input.txt","rt")

n = int(input())
inputList = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
res= ""
tmp = []
cnt = 0

while lt <= rt :
    if last < inputList[lt] :
        tmp.append((inputList[lt],'L'))
    if last < inputList[rt] :
        tmp.append((inputList[rt], 'R'))
    if len(tmp) == 0 :
        break

    tmp.sort()
    res += tmp[0][1]
    if(tmp[0][1] == 'L') :
        lt +=1
    else :
        rt -= 1
    last = tmp[0][0]
    tmp.clear()

# print(len(res))
# print(res)
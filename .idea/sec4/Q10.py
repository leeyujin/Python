# 역수열(그리디)
#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
inputList = list(map(int, input().split()))

batched = [0]*n

for i in range(n) :

    #들어가야할 위치
    idx = inputList[i]
    #들어갈 값
    val = i + 1

    # 5까지
    cnt = 0
    inputIdx = 0
    for j in range(n) :
        # 해당 if 문 뒤 or batched[j] > val  는 필요없음. 작은수부터 넣는것
        if batched[j] == 0 :
            cnt += 1
        if cnt == idx :
            #다음 idx에 값 삽입
            inputIdx = j+1
            break

    # 비어있는지 여부 확인 후 삽입
    for j in range(inputIdx, n) :
        if batched[j] == 0 :
            batched[j] = val
            break
for i in batched :
    print(i, end=" ")
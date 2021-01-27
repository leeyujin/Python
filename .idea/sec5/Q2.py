# 쇠막대기
#import sys
#sys.stdin = open("input.txt","rt")

a = list(input())
latest = ''
stack = []
cnt = 0
tmp = 0
for i in a :
    tmp += 1
    if i == '(' :
        stack.append(i)
    else :
        # 레이저
        if latest == '(' :
            stack.pop()
            cnt += len(stack)
        # 오른쪽 기둥
        else :
            stack.pop()
            cnt += 1

    latest = i

print(cnt)
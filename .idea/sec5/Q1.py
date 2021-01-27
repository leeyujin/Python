#가장 큰 수
import sys
sys.stdin = open("input.txt","rt")

n,m= map(int, input().split())
a = list(map(int, str(n)))

stack = []

for i in a :

    while stack and m > 0  and stack[-1] < i:
        m -= 1
        stack.pop()

    stack.append(i)

if m > 0 :
    stack = stack[:-m]

res = ''.join(map(str,stack))
print(res)


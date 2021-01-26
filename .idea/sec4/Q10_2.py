import sys
sys.stdin = open("input.txt","rt")
n = int(input())

a =list(map(int,input().split()))

a = a[::-1]

print(a)
ans=[]

for x in a:

    ans.insert(x,n)

    n -=1

print(ans)
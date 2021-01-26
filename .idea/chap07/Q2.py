import sys
sys.stdin = open("input.txt","rt")
n=int(input())
a= list(map(int, input().split()))
m=int(input())
b = list(map(int,input().split()))


a.sort()

def printYesOrNo(num) :

    lt , rt = 0, len(a) -1

    while lt <= rt :
        mid = ( lt + rt ) // 2
        midVal = a[mid]
        if midVal < num :
            lt = mid +1
        elif midVal > num :
            rt = mid - 1
        else :
            print("YES")
            return
    print("NO")



for i in b :
    printYesOrNo(i)

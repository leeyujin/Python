#import sys
#sys.stdin= open("input.txt","rt")
T=int(input())
ansList = []
for i in range(T):
    N,s,e,k = map(int, input().split())

    # int 리스트로 어떻게 받는지?  - string 리스트로 받으니 사전형식 sort됨
    #inputList = input().split()
    inputList = list(map(int,input().split()))

    subList = inputList[s-1:e]
    subList.sort()
    #print(subList)
    ansList.append(subList[k-1])

for i in range(T):
    #이렇게 출력하는게 최선?
    #print("#" + str(i+1) + " " + str(ansList[i]) )
    print("#%d %d" %((i+1), ansList[i]))



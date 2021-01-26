#import sys
#sys.stdin=open("input1.txt","rt")
N,K = map(int, input().split())

def getDivisorList(x) :
    divisorList = list();
    for i in range(1,x+1) :
        if x % i == 0 :
            divisorList.append(i)
    return divisorList

divisorList=getDivisorList(N)
divisorCnt = len(divisorList)
if( divisorCnt < K ) :
    print(-1)
else :
    print(divisorList[K-1])

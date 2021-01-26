import sys
sys.stdin = open("input.txt","rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

start , end = 0, n-1

while start <= end :
    mid = (start+end)//2

    if a[mid] == m :
        print(mid+1)
        break
    elif a[mid] < m :
        start = mid+1
    else :
        end = mid-1



''' 함수형
def findNum(arr,target,start,end) :
    if( start >  end ):
        return None

    mid = ( start + end  ) // 2

    if( arr[mid] == target ) :
        return mid+1

    elif( target < arr[mid] ) :
        return findNum(arr,target,start,mid-1)

    else :
        return findNum(arr,target,mid+1,end)

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

print(findNum(a,m,0,n-1))

'''
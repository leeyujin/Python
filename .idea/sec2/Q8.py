import sys
sys.stdin=open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))


def reverse(x):
    b = list()
    for i in str(x):
        b.append(i)
    b.reverse()
    c = ""
    for i in b :
        c += i
    return int(c)

def reverse2(x):
    res=0
    while x > 0 :
        t = x%10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x) :
    if x==1 :
        return False
    ''' 절반까지만 돌아도됨 - 약수 
    for i in range(2,x) :
        if x%i==0 :
            return False
    '''
    for i in range(2, x//2 +1) :
        if x%i==0:
            return False
    else :
        return True

for i in a :
    reversedNum = reverse2(i)
    if(isPrime(reversedNum)) :
        print (reversedNum, end=" ")

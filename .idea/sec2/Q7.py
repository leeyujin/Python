#import sys
#sys.stdin=open("input.txt","rt")
n = int(input())

''' 시간초과
def isPrime(x) :
    for i in range(2,x) :
        if x%i == 0 :
            return False
    return True

a = list()

for i in range(2,n+1):
    if(isPrime(i)) :
        cnt += 1
'''

ch = [0] * (n+1)
cnt = 0

for i in range(2,n+1) :
    if (ch[i] == 0) :
        cnt += 1
        '''시간초과 
        for j in range(i, n+1) :
            if ( i * j ) <= n :
                ch[i*j] += ch[i*j] +1
        '''
        for j in range(i,n+1,i):
            ch[j] += ch[j]+1
print(cnt)
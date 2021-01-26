import sys
sys.stdin = open("input.txt","rt")

n,m=map(int,input().split())
a=list(map(int,input().split()))

lt = cnt = 0
tot=a[lt]
rt = 1
lenA = len(a)
while True:
    if tot < m :
        if rt < lenA :
            tot += a[rt]
            rt += 1
        else :
            break
    elif tot == m :
        cnt += 1
        #print("%d %d %d" %(lt, rt-1,tot))
        tot -= a[lt]
        lt += 1
    else :
        tot -= a[lt]
        lt += 1

print(cnt)


''' timeover
lenA = len(a)
cnt = 0
sum1 = 0

for i in range (0, lenA) :
    p2 = i+1
    sum1 = 0
    while sum1 < m  and p2 <= lenA:
        sum1 = sum( a[i:p2] )
        #print(a[i:p2])
        #print(sum1)
        p2 +=1
        if(sum1 == m ) :
            cnt+=1
            break

print(cnt)
'''

''' timeover
for idx1 in range(0, lenA) :
    temp1=a[idx1]
    sum=0
    sum += temp1
    if m == sum :
       cnt +=1
       continue
    if( m > sum ) :
       for idx2 in range(idx1+1, lenA) :
           temp2=a[idx2]
           sum += temp2
           if( m == sum) :
                cnt +=1
                break
           elif( sum > m) :
               break
    else :
        continue

print(cnt)
'''
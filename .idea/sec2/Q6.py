import sys
sys.stdin=open("input.txt", "rt")
n = map(int, input().split())
a = list(map(int,input().split()))


def digit_sum(x) :
    # 나처럼 str으로 받아서 하려나?
    intToStr = str(x)
    length = len(intToStr)
    sum = 0
    ''' - string은 바로 접근가능
    for i in range(length) :
        sum += int( intToStr[i:i+1] )
    '''
    for i in intToStr :
        sum += int(i)
    return sum

def digit_sum2(x) :
    sum = 0
    while x > 0 :
        sum += x%10
        x = x//10
    return sum

b = list()
for i in a :
    b.append(digit_sum2(i))
idx = b.index( max(b) )

# sol 2
max = -2147000000
res = 0
for i in a :
    tot=digit_sum2(i)
    if max < tot :
        max = tot
        res = i

print( res)
#import sys
#sys.stdin = open("input.txt","rt")
n = map(int, input().split())
a = list(map(int, input().split()))

len = len(a)
sum = 0

for i in a :
    sum += i

'''
    round는 round_half_even 방식을 택한다
    따라서 round 말고
    a = 66.5
    a += 0.5
    a = int(a) 처럼 하자
'''
avg = round(sum/len)

diff = 101
score = 0 # 점수
num = 0 #학생 번호

for index,value in enumerate(a) :
    diff2 = abs( value - avg )
    if ( diff2 < diff ) :
        diff = diff2
        score = value
        num = index
    elif( diff2 == diff ) :
        if ( score < value ) :
            num = index
            score = value

print(avg, num+1, sep=" ")

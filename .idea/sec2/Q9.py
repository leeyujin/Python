#import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
a=list()
for i in range(0,n) :
    a.append(list(map(int,input().split())))

b=list()
for i in range(0,n) :
    #z,x,c = map(int, input().split())
    num1 = a[i][0]
    num2= a[i][1]
    num3= a[i][2]

    award = 0

    rule1= num1 == num2 == num3
    rule2 = (num1 == num2) or (num1 == num3) or (num2==num3)
    rule3 = num1 != num2 and num2 != num3

    if(rule1) :
        award = 10000 + num1 * 1000
    elif(rule2) :
        samenum=0
        if(num1==num2) :
            samenum=num1
        elif(num1 == num3) :
            samenum = num1
        else :
            samenum=num2
        award = 1000 + samenum *100
    elif(rule3) :
        award = max(num1,num2,num3)*100

    b.append(award)

print(max(b))
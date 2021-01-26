import sys
sys.stdin = open("input.txt", "rt")
n = int(input())

'''A1
for i in range(n) :
    s = input().upper()

    for j in range( len(s)//2) :
        if s[j] != s[-1-j] :
            print("#%d NO" %(i+1))
    else :
        print("#%d YES" %(i+1))

'''

#A2
for i in range(n) :
    s = input().upper()

    if s == s[::-1] :
        print("#%d YES" %(i+1))
    else :
        print("#%d NO" %(i+1))










''' 내가 풀이한 것 
a= list()
for i in range(n) :
    a.append( input())

b = list()
for strA in a :
    lenA = len(strA)
    for i in range(0, lenA) :
        head = strA[i].upper()
        tail = strA[lenA-i-1].upper()
        middle = int(lenA/2)
        if middle < lenA-i :
            if head != tail :
                b.append("NO")
                break
            else :
                continue
        else :
            b.append("YES")
            break
for idx,val in enumerate(b) :
    print("#%d %s" %((idx+1),val))

'''
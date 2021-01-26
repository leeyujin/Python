import sys
sys.stdin = open("input.txt","rt")

a = list(range(21))

for _ in range(10) :
    s,e = map(int,input().split())
    for j in range(0, (e-s+1)//2) :
        a[s+j] , a[e-j] = a[e-j], a[s+j]
a.pop(0)
for j in a :
    print(j, end=" ")


'''
a = [0]*21

for i in range(1,21) :
    a[i] = i

b = list()
for i in range(0,10) :
    b.append( list(map(int, input().split())) )

for i in b :
    ai = i[0]
    bi = i[1]
    len = int((bi - ai)/2 + 0.5)
    for k in range(0,len) :
        tempa = a[ai + k]
        tempb = a[bi - k]
        a[ai+k] = tempb
        a[bi-k] = tempa
        #print("%d %d" %(tempa, tempb))
        #print(a)

a.remove(0)
for j in a :
    print(j, end=" ")
'''
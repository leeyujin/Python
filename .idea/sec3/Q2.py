import sys
sys.stdin=open("input.txt","rt")

inputStr=input()
res = 0
for i in inputStr :
    if i.isdecimal() :
        res = res*10 + int(i)

print(res)
cnt = 0
for i in range(1,res+1) :
    if res % i == 0 :
        cnt+=1

print(cnt)



'''
a = "";
for i in inputStr:
    if i.isnumeric() :
       a +=i

a = int(a)
cnt = 2

for i in range(2,a) :
    if a % i == 0 :
        cnt += 1


print (a)
print (cnt)
'''
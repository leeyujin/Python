a=[23,12,36,53,19]
print(a[:2])
print(a[2:5])

for i in range(len(a)) :
    print(a[i], end=' ')

print()

for x in a :
    print (x, end=' ')

print()

b = (1,2,3,4,5)
#b[1]=3 - tuple값은 변경할수 없음

for x in enumerate(a):
    print (x[0], x[1], end=' ')

print()

for index,value in enumerate(a):
    print (index, value, end=' ')

print()

if all( x<60 for x in a):
    print("YES")
else :
    print("NO")

if any( x<13 for x in a):
    print("YES")
else :
    print("NO")

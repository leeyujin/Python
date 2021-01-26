a=[0]*3
print(a)

a=[[0]*3 for _ in range(3)]
print(a)

a[0][1]=1
a[1][1]=2

for x in a :
    for y in x:
        print(y, end=" ")
    print()

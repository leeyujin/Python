def isPrime(x):
    for i in range(2,x):
        if(x%i == 0):
            return False
    return True

a = [12,13,15,16,39,41]
for x in a:
    if isPrime(x):
        print(x, end=" ")


def plus_one(x):
    return x+1

b = list(range(5))
print ( list(map(plus_one, b)) )
print ( list(map( lambda x:x+1, b)) )


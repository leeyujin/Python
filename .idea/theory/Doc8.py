import random as r
a = list(range(1,6))
b = [6,7]
c = a+b

print(a)
a.append(6) # 리스트 끝에 추가
print(a)
a.insert(3,7) #3번 index에 insert
print(a)
a.pop()
print(a)
a.pop(3)  # 3번 index remove
print(a)
a.remove(4)  # 값이 4인것 remove
print(a)

print(sum(a))
print(max(a))
print(min(a))

a = list(range(1,11))
r.shuffle(a) # random shuffle
print(a)
a.sort() #오름차순
print(a)
a.sort(reverse=True)
print(a) # 내림차순
a.clear()
print(a)
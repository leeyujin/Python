i = 'It is Time'
print(i.upper()) # 대문자
print(i.lower()) # 소문자
print(i.find('T')) # lowest index
print(i.count('T')) # 개수 2
print(i[:2]) #0~1까지 출력
print(i[3:5]) #3~4까지 출력
print('A'.isalpha()) # 알파벳여부
print(ord('A')) # chr -> ASCII
print(chr(65)) # ASCII -> chr



a=list[1,2,3,3,3,'A',5,'BCD']
print(a)
a.remove(int(3))
print(a)
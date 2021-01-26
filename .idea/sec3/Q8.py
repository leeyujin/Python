import sys,copy
sys.stdin = open("input.txt", "rt")


'''
 1. 왼쪽일 때 
     a,b,c 
    for i in n
       mv = i + c -1
       if mv > len -1
        mv = mv - len  
       
 2. 오른쪽 일 때
   for i in n
       mv = i - c + 1 ( 0 - 3 + 1 = -2 )
       if mv < len - 1
        mv = mv + len ( -2 + 5 = 3 )

3. 합 구하기    
    s = 0
    e = len 
    for i in range(a)
        for j in range(s,e)
            list[s] + list [e]
        if i <= s+e // 2 :
            s += 1
            e -= 1
        else : 
            s -= 1
            e += 1
                
'''

n = int(input())

numList = [ list(map(int, input().split())) for _ in range(n) ]

m = int(input())

rotateList = [ list(map(int,input().split())) for _ in range(m) ]


for i in range(m) :
    a = rotateList[i][0]
    b = rotateList[i][1]
    c = rotateList[i][2]

    tempList = copy.deepcopy(numList)


    #왼쪽
    if b == 0 :
        for j in range(n) :
            mv = j + c -1
            if mv > n -1 :
                mv -= n
            tempList[a-1][mv] = numList[a-1][j]
        numList[a-1] = tempList[a-1]

    else :
        for j in range(n) :
            mv = j - c + 1
            # print( "mv : %d, j : %d , c :  %d " %( mv, j , c))
            if mv < 0 :
                mv += n
            tempList[a-1][mv] = numList[a-1][j]
        numList[a-1] = tempList[a-1]

print(numList)
s = 0
e = n
sum = 0
for i in range(n) :
    for j in range(s,e) :
        print(numList[i][j])
        sum += numList[i][j]
    if i < (n // 2) :
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1

print(sum)


















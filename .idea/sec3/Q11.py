#import sys
#sys.stdin = open("input.txt","rt")

a = [ list(map(int, input().split())) for _ in range(7) ]
cnt = 0

#행
for i in range(7) :
    for j in  range(3) :
        x , y = i , 5+j
        temp = a[x][j:y]
        # print(temp)
        if(temp == temp[::-1]) :
            cnt+=1

#열
for i in range(7):
    for j in range(3) :
        b = list()
        for k in range(5) :
            x , y= j+k, i
            b.append( a[x][y] )
        # print(b)
        if(b == b[::-1]) :
            cnt+=1


# for z in range (7) :
#     for i in range(3) :
#         b = list()
#         c = list()
#         for j in range(5) :
#             x,y = z+i, i+j
#             m,n = i+j , z+i
#             b.append(a[x][y])
#             c.append(a[m][n])
#         # 행 검사
#         if (b == b[::-1]) :
#            cnt +=1
#         # 열 검사
#         if( c == c[::-1]) :
#             cnt +=1

print(cnt)
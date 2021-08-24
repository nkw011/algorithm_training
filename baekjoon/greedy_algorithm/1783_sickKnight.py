# 방문할 수 있는 모든 칸의 개수가 아닌 한 번에 최대로 갈 수 있는 칸의 개수를 가리킨다.

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
if n == 1:
    print(1)
elif n == 2 :
    print(min(4,1+(m-1)//2))
else :
    if m <= 3 :
        print(m)
    elif 4<=m<= 6:
        print(4)
    else :
        print(m-2)
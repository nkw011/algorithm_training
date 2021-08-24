import sys
input = sys.stdin.readline
from collections import deque

# 3개를 동시에 할려면 3차원 table이 필요할 수도 있으니 다른 방법으로 dictionary를 이용하는 방법을 택했다,
a,b,c = map(int,input().split())
dic = {}
def bfs():
    dic[(a,b,c)] = True
    q = deque()
    q.append((a,b,c))
    sums = a+b+c
    while q:
        n1,n2,n3 = q.popleft()
        if n1 == n2 and n2 == n3:
            return 1
        for x,y in [(n1,n2),(n2,n3),(n1,n3)]:
            if x == y:
                continue
            elif x > y:
                x -= y
                y *= 2
            elif x < y:
                y -= x
                x *= 2
            z = sums - (x+y)
            if (x,y,z) not in dic.keys() :
                dic[(x,y,z)] = True
                q.append((x,y,z))
    return 0

print(bfs())

#
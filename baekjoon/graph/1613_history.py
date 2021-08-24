# 만약 테스트케이스가 1,1이 들어왔을 때 1은 1보다 먼저 일어나거나 나중에 일어난 것이 아니기 때문에
# 같은 사건이 들어오면 0이 나와야한다.
# 힌트를 보고 풀면 안된다.
# 힌트를 보고 푸니까 문제를 깊게 고민 안하게 되는 것 같다.
# 입력 값이 작은 범위에서 길이 존재하거나 최단거리를 알아봐야하는 문제가 나올 때 플로이드-와샬 알고리즘을 사용해보자

import sys
input = lambda : sys.stdin.readline().rstrip()
INF = 400 * 400


n,k = map(int,input().split())
dist = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    dist[a][b] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][k] + dist[k][j],dist[i][j])

s = int(input())
for _ in range(s):
    a,b = map(int,input().split())
    if dist[a][b] != INF:
        print(-1)
    elif dist[b][a] != INF:
        print(1)
    else :
        print(0)

        
############ 테스트 코드 ######################
import random
INF = 400 * 400

def myResult(n,k,edges,r,c):
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for a,b in edges:
        dist[a][b] = 1
        
    # 결국 이 부분이 틀린 것이다.
    for i in range(1,n+1):
        dist[i][i] = 0
        
    # 두번째로 인덱스 탐색범위를 0 ~ n 까지 담은 것이 틀린것이다.
    # 1 ~ n+1로 해야됨
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j] = min(dist[i][k] + dist[k][j],dist[i][j])
    
    if dist[r][c] != INF:
        return -1
    elif dist[c][r] != INF:
        return 1
    else :
        return 0
        
# 정답 코드 출처: https://chldkato.tistory.com/35
def answer(n,m,edges,r,c):
    a = [[0]*n for _ in range(n)]
    
    for x,y in edges:
        a[x-1][y-1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if a[i][k] and a[k][j]:
                    a[i][j] = 1
    
    if a[r-1][c-1] == 1:
        return -1
    elif a[c-1][r-1] == 1:
        return 1
    elif a[r-1][c-1] == 0:
        return 0

def test():
    while True:
        n = random.randrange(1,6)
        k = random.randrange(1,10)
        edges = []
        for _ in range(k):
            a,b = random.randrange(1,n+1),random.randrange(1,n+1)
            edges.append((a,b))
        s = random.randrange(1,10)
        ts = []
        possible = True
        for _ in range(s):
            a,b = random.randrange(1,n+1),random.randrange(1,n+1)
            r1 = myResult(n,k,edges,a,b)
            r2 = answer(n,k,edges,a,b)
            
            if r1 != r2:
                possible = False
                print("n:",n)
                print("edges:",edges)
                print("a:",a,"b:",b,"r1:",r1,"r2:",r2)
                break
        if not possible:
            break
        
test()
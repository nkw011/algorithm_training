import sys
def input(): return sys.stdin.readline().rstrip()

# 문제 풀이
# 1. 각 건물들 사이의 기울기를 모두 구한다.
# 2. 고층 빌딩 A에서 고층 빌딩 B를 보려면
#   * A와 B 사이의 빌딩을 K라고 지칭할 때
#   2.1. B가 A의 왼쪽에 있는 경우: K와 A의 기울기가 B와 A의 기울기보다 같거나 작으면 보지 못한다
#   2.2. B가 A의 오른쪽에 있는 경우: K와 A의 기울기가 B와 A의 기울기보다 같거나 크면 보지 못한다

n = int(input())
buildings = list(map(int,input().split()))
grad = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: continue
        grad[i][j] = (buildings[i] - buildings[j]) / (i-j)
max_cnt = [0] * n
for i in range(n):
    cnt = 0
    for l in range(i):
        possible = True
        for k in range(l+1,i):
            if grad[k][i] <= grad[l][i]:
                possible = False
        if possible: cnt += 1
    for r in range(i+1,n):
        possible = True
        for k in range(i+1,r):
            if grad[i][k] >= grad[i][r]:
                possible = False
        if possible: cnt += 1
    max_cnt[i] = cnt
print(max(max_cnt))

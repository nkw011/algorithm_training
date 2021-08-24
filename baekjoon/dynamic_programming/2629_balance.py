# 추가 있는 쪽에, 추가 없는 쪽에, 둘 다 놓지 않는다.
# dp cache를 활용하지 않고 갱신하려고 하니 시간초과가 나왔다.
# 답을 보았다고 해서 너무 답에 의존하려고 하지 말자..
# 내가 그 아이디어를 꼼꼼히 구현하였는지 놓친 부분은 없는지 면밀히 살펴보자
# (발생되는 문제점들)


import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(100000)


def balance(i, weight):
    if dp[i][weight]:
        return
    dp[i][weight] = 1
    if i == n:
        return
    balance(i+1, weight)
    balance(i+1, weight+w[i])
    balance(i+1, abs(w[i]-weight))


n = int(input())
w = list(map(int, input().split()))
k = int(input())
tgt = list(map(int, input().split()))
leng = sum(w)

dp = [[0] * (leng+1) for _ in range(n+1)]

balance(0, 0)

for t in tgt:
    if t > leng or not dp[n][t]:
        print("N", end=' ')
    elif dp[n][t]:
        print("Y", end=' ')

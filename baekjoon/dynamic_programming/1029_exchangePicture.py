import sys
def input(): return sys.stdin.readline().rstrip()


# 단순하게 dp의 차원 수는 파라미터 숫자와 같다.
def exchange(i, price, visited):
    if dp[i][visited][price] != -1:
        return dp[i][visited][price]
    dp[i][visited][price] = 0
    for nxt in range(n):
        if visited & (1 << nxt):
            continue
        if sell[i][nxt] >= price:
            dp[i][visited][price] = max(
                dp[i][visited][price], 1+exchange(nxt, sell[i][nxt], visited | (1 << nxt)))
    return dp[i][visited][price]


n = int(input())
sell = [list(map(int, input())) for _ in range(n)]
# 즉 어떤 사람이 그림을 살 수 있다면 무조건 체크해주는 것이 아닌
# 그 중에 가장 낮은 가격으로 사는 사람을 사야 많이 살 수 있다.
# 이런 것을 체크하지 않으면 visited에 price를 넣어주어야한다. 마지막으로 이 가격일 때의 값 등등
dp = [[[-1] * 10 for _ in range((1 << n))] for _ in range(n)]
print(1+exchange(0, 0, 1))

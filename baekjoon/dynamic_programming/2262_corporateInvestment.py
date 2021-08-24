import sys
input = lambda: sys.stdin.readline().rstrip()

# 꼭 지금 상태에서의 최댓값이 전체 답안의 최댓값을 보장하는 것이 아니기 때문에
# 역추적하는 방식으로 하는 것이 좋다.

def dpStock(i, money):
    if i == m: return 0
    if dp[i][money] != -1: return dp[i][money]
    dp[i][money] = 0
    # 이 기업의 종목을 투자하는 경우
    for mon in range(1, money + 1):
        if dp[i][money] < profit[mon][i] + dpStock(i + 1, money - mon):
            dp[i][money] = profit[mon][i] + dpStock(i + 1, money - mon)
            price[i][money] = mon
    # 이 기업의 종목을 투자하지 않는 경우
    if dp[i][money] < dpStock(i + 1, money):
        dp[i][money] = dpStock(i + 1, money)
        price[i][money] = 0
    return dp[i][money]

def printPrice():
    i = 0
    money = n
    while i < m:
        print(price[i][money], end=' ')
        money -= price[i][money]
        i += 1
    print()

n, m = map(int, input().split())
profit = [[0] * m for _ in range(n + 1)]
dp = [[-1] * (n + 1) for _ in range(m)]
price = [[0] * (n+1) for _ in range(m)]


for _ in range(n):
    comp = list(map(int, input().split()))
    for i in range(m):
        profit[comp[0]][i] = comp[i+1] 

parent = [0] * m
print(dpStock(0, n))
printPrice()
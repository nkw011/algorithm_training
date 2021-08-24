import sys
from collections import deque
input = sys.stdin.readline

# 증가하는 부분 수열을 만들면 될 것 같다.
# 굳이 하나씩 담지 않고 바로바로 계산을 했으면 되었을 것 같은데.... 난 바보다
# 훨씬 코드 길이가 간단할텐데....ㅠㅠ

T = int(input().rstrip())
for loop in range(T):
    n = int(input().rstrip())
    stocks = list(map(int,input().split()))

    now = n-1
    i = n-2
    wallet = []
    result = 0
    while i >= 0:
        if stocks[i] <= stocks[now]:
            wallet.append(stocks[i])
        else :
            if len(wallet) > 0:
                for money in wallet:
                    result += (stocks[now] - money)
                wallet = []
            now = i
        i -= 1
    if len(wallet) > 0:
        for money in wallet:
            result += (stocks[now] - money)
    print(result)
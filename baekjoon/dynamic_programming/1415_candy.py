# 같은 값이 여러가지 있다는 것이 2624번과 매우 흡사하다.
# 중복된 값이 여러가지 있을 때의 경우의 수 구하기인 것 같다.

import sys
import math
def input(): return sys.stdin.readline().rstrip()


def isPrime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for d in range(3, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

# 꼭 i가 dp에 필요한 건 아닌 것 같다.
# 메모리 사용량을 줄일 수도 있을 것 같다.


def candy(i, p):
    if i >= tot:
        return prime[p]
    if dp[i][p] != -1:
        return dp[i][p]
    dp[i][p] = 0
    for c in range(cnt[price[i]]+1):
        dp[i][p] += candy(i+1, p+price[i] * c)
    return dp[i][p]


n = int(input())
price = []
tot = 0
cnt = [0] * 10001
priceSum = 0

for _ in range(n):
    p = int(input())
    priceSum += p
    if cnt[p] == 0:
        price.append(p)
        tot += 1
    cnt[p] += 1

prime = [0] * (priceSum+1)
for i in range(1, priceSum+1):
    if isPrime(i):
        prime[i] = 1

dp = [[-1] * (priceSum+1) for _ in range(tot)]
print(candy(0, 0))

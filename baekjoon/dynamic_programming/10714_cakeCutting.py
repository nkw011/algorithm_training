# 시계방향 이동 : (i-1+n) % n 반시계방향 이동: (i+1)%n
# JOI와 IOI가 얻는 점수를 나처럼 하나의 함수로 구하는 것이 아닌 두 개의 함수로 나누는 것도 괜찮은 것 같다.
# 그리고 두 개의 함수로 나눌경우 dp도 2차원 table로 만들면 된다. -> 두 개로 나눈게 시간으로도 빠르고 메모리로도 좋다.

import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(100000)


def game(l, r, myturn):
    # 그렇네... 같을 때가 결국 마지막 선택이므로 내 차례이면 cake 크기를 반환하고 아니면 0을 반환하면 된다.
    if l == r:
        if myturn:
            return cake[r]
        return 0
    if dp[l][r][myturn] != -1:
        return dp[l][r][myturn]
    dp[l][r][myturn] = 0
    if myturn:
        dp[l][r][myturn] = max(dp[l][r][myturn], cake[l] +
                               game((l+1) % n, r, 0))
        dp[l][r][myturn] = max(dp[l][r][myturn], cake[r] +
                               game(l, (r-1+n) % n, 0))
    else:
        if cake[l] > cake[r]:
            dp[l][r][myturn] = max(
                dp[l][r][myturn], game((l+1) % n, r, 1))
        else:
            dp[l][r][myturn] = max(dp[l][r][myturn], game(l, (r-1+n) % n, 1))
    return dp[l][r][myturn]


n = int(input())
cake = [int(input()) for _ in range(n)]

result = 0
dp = [[[-1] * 2 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    left, right = (i+1) % n, (i-1+n) % n
    result = max(result, cake[i] + game(left, right, 0))

print(result)

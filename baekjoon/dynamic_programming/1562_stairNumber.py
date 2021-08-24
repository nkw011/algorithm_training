# 비트마스크를 활용할 때 주의가 필요하다!
# 어떤 원소를 추가할 때 중복 추가하지 않기 위해서는 '|'을 사용해야한다. 


import sys
REMINDER = 1000000000
def input(): return sys.stdin.readline().rstrip()


def stairNumber(num, length, allHave):
    if length == 0:
        if allHave == (1 << 10) - 1:
            return 1
        return 0
    if dp[num][length][allHave] != -1:
        return dp[num][length][allHave]
    dp[num][length][allHave] = 0

    if num-1 >= 0:
        dp[num][length][allHave] += stairNumber(
            num-1, length-1, allHave | 1 << (num-1))
    if num+1 <= 9:
        dp[num][length][allHave] += stairNumber(
            num+1, length-1, allHave | 1 << (num+1))
    dp[num][length][allHave] %= REMINDER
    return dp[num][length][allHave]


n = int(input())
dp = [[[-1] * ((1 << 10)+1) for _ in range(n+1)] for _ in range(10)]
result = 0
for num in range(1, 10):
    result += stairNumber(num, n-1, (1 << num))
print(result % REMINDER)

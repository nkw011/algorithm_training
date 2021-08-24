import sys
NEGINF = -(10**52)
POSINF = 10 ** 52
def input(): return sys.stdin.readline().rstrip()


def findMax(digit, remain):
    if remain == 0:
        return 0
    if remain < 2:
        return NEGINF
    if dp[digit][remain] != -1:
        return dp[digit][remain]
    dp[digit][remain] = NEGINF
    for i in range(10):
        if remain >= match[i]:
            dp[digit][remain] = max(
                dp[digit][remain], i + 10 * findMax(digit+1, remain-match[i]))
    return dp[digit][remain]


def findMin(digit, remain):
    if remain == 0:
        return 0
    if remain < 2:
        return POSINF
    if dp2[digit][remain] != -1:
        return dp2[digit][remain]
    dp2[digit][remain] = POSINF
    for i in range(10):
        # 맨 처음에 0이 오면 안된다. -> 이걸 제대로 고려를 하지 못했다.
        if i == 0 and remain <= 6:
            continue
        if remain >= match[i]:
            dp2[digit][remain] = min(
                dp2[digit][remain], i + 10 * findMin(digit+1, remain-match[i]))
    return dp2[digit][remain]


match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
T = int(input())
for _ in range(T):
    n = int(input())
    limit = n//2 + 1 if n % 2 == 0 else n//2 + 2
    dp = [[-1] * (n+1) for _ in range(limit)]
    dp2 = [[-1] * (n+1) for _ in range(limit)]

    result1 = POSINF
    # 한 자리일 때는 0이오면 안된다. 2자리 이상일 때는 0이 마지막 숫자로 와도 된다.
    # 요구사항을 제대로 반영하면서 구현을 제대로 하지 못하였다...
    if n <= 6:
        for num in range(1, 10):
            result1 = min(result1, num + 10*findMin(1, n-match[num]))
    else:
        for num in range(10):
            result1 = min(result1, num + 10*findMin(1, n-match[num]))

    result2 = 0
    for num in range(1, 10):
        result2 = max(result2, num + 10*findMax(1, n-match[num]))

    print(result1, result2)

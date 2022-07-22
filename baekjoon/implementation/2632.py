# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-2632
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-2632/

import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

def find_case(pizza, length):
    case = defaultdict(int)
    for i in range(length):
        temp = pizza[i:] + pizza[:i]
        pre = 0
        for num in temp:
            pre += num
            case[pre] += 1
    case[sum(pizza)] = 1
    return case

k = int(input())
n, m = map(int,input().split())
pizza_a = [int(input()) for _ in range(n)]
pizza_b = [int(input()) for _ in range(m)]

case1 = find_case(pizza_a, n)
case2 = find_case(pizza_b, m)

result = case1.get(k, 0) + case2.get(k, 0)
for num in case1:
    if k-num in case2:
        result += case1[num] * case2[k-num]
print(result)

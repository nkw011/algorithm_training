import sys
from collections import Counter
def input(): return sys.stdin.readline().rstrip()


n = int(input())
nums = list(map(int, input().split()))
counter = Counter(nums)
cnt = 0

for num in nums:
    counter[num] -= 1
    for d in counter:
        counter[d] -= 1
        if counter[d] >= 0 and (num-d) in counter and counter[num-d] > 0:
            counter[d] += 1
            cnt += 1
            break
        counter[d] += 1
    counter[num] += 1
print(cnt)

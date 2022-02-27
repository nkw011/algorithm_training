import sys
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()


a, b = input().split()
b = int(b)

target = -1
for arr in permutations(a, len(a)):
    if arr[0] == '0':
        continue
    number = int("".join(arr))
    if target < number <= b:
        target = number
print(target)

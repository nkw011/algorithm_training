import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array = [m] * m
values = []
elem = []
for _ in range(n):
    elem = list(map(int,input().split()))
    for i in range(m):
        if elem[i] == 0:
            array[i] -= 1
    values.append(elem[:])
possible = True
for arr in values:
    minOne = m
    for i in range(m):
        if arr[i] == 1 and minOne > array[i]:
            minOne = array[i]
    for i in range(m):
        if arr[i] == 0 and minOne <= array[i]:
            possible = False
            break
    if not possible:
        print("NO")
        break
if possible:
    print("YES")
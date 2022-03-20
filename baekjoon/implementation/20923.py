import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
deck = [deque(), deque()]
ground = [list(), list()]
for _ in range(n):
    d, s = map(int, input().split())
    deck[0].appendleft(d)
    deck[1].appendleft(s)

for i in range(m):
    ground[i % 2].append(deck[i % 2].popleft())
    # 그라운드로 옮기고 나서도 덱의 갯수가 0이 되면 바로 끝난다. -> 즉 빈 덱을 체크하는 것을 뽑고 나서 해야한다.
    if not deck[i % 2]:
        break
    if (ground[0] and ground[1]) and ground[0][-1] + ground[1][-1] == 5:
        deck[1].extend(ground[0])
        deck[1].extend(ground[1])
        ground[0].clear()
        ground[1].clear()
    elif (ground[0] and ground[0][-1] == 5) or (ground[1] and ground[1][-1] == 5):
        deck[0].extend(ground[1])
        deck[0].extend(ground[0])
        ground[0].clear()
        ground[1].clear()
dodo_len, suyeon_len = len(deck[0]), len(deck[1])
if dodo_len > suyeon_len:
    print('do')
elif dodo_len == suyeon_len:
    print('dosu')
else:
    print('su')

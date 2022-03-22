import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def rotate_counter(i):
    wheel[i].append(wheel[i].popleft())


def rotate_clock(i):
    wheel[i].appendleft(wheel[i].pop())


def left_check(idx, num, direc):
    if idx < 0:
        return
    if wheel[idx][2] != num:
        left_check(idx-1, wheel[idx][6], -direc)
        rotate[-direc](idx)


def right_check(idx, num, direc):
    if idx >= 4:
        return
    if wheel[idx][6] != num:
        right_check(idx+1, wheel[idx][2], -direc)
        rotate[-direc](idx)


wheel = [deque(list(input())) for _ in range(4)]

rotate = {1: rotate_clock, -1: rotate_counter}

for _ in range(int(input())):
    num, direc = map(int, input().split())
    num -= 1
    if num-1 >= 0:
        left_check(num-1, wheel[num][6], direc)
    if num+1 < 4:
        right_check(num+1, wheel[num][2], direc)
    rotate[direc](num)
result = 0
for i in range(4):
    if wheel[i][0] == '1':
        result += (2**i)
print(result)

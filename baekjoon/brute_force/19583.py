import sys
def input(): return sys.stdin.readline().rstrip()


def time2minute(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)


s, e, q = map(time2minute, input().split())

cond1, cond2 = set(), set()
while True:
    try:
        t, p = input().split()
        t = time2minute(t)
        if t <= s:
            cond1.add(p)
        if e <= t <= q:
            cond2.add(p)
    except:
        break

print(len(cond1 & cond2))

import sys
input = sys.stdin.readline

day = 0
while True:
    day += 1
    n = int(input().rstrip())
    if n == 0:
        break
    parties = [tuple(map(int,input().split())) for _ in range(n)]
    parties = sorted(parties,key=lambda x:(x[1],x[0]))
    count = 0
    visited = [0] * n
    for time in range(8,25,0.5):
        index = 0
        while index < n:
            if parties[index][0] > time:
                break
            if time + 0.5 <= parties[index][1]:
                count += 1
                visited[index] = 1
    print("On day {0} Emma can attend as many as {1} parties.".format(day,count))
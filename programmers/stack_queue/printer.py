from collections import deque

def solution(priorities,location):
    priorities = deque(priorities)
    cnt = 0
    locations = deque(list(range(len(priorities))))
    while priorities:
        p = priorities.popleft()
        loc = locations.popleft()
        able = True
        for other in priorities:
            if other > p:
                priorities.append(p)
                locations.append(loc)
                able = False
                break
        if able:
            cnt += 1
            if loc == location:
                return cnt

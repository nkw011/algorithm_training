import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
for loop in range(T):
    n = int(input().rstrip())
    logs = list(map(int,input().split()))
    logs.sort()
    newLogs = deque()
    newLogs.append(logs[0])
    for i in range(1,n):
        if i % 2 == 0 :
            newLogs.appendleft(logs[i])
        else:
            newLogs.append(logs[i])
    difference = 0
    for i in range(1,n):
        difference = max(difference,abs(newLogs[i]-newLogs[i-1]))
    difference = max(difference,newLogs[n-1]-newLogs[0])
    print(difference)
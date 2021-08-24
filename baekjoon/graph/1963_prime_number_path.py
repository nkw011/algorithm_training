import sys,math
input = sys.stdin.readline
from collections import deque

def isPrime(num):
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def bfs():
    global num1,num2
    visited[num1] = 1
    q = deque()
    q.append((num1,0))
    while q:
        number,count = q.popleft()
        if number == num2:
            return count
        for i in range(3,-1,-1):
            for j in range(10):
                if i == 3 and j == 0 :
                    continue
                newNum = (j *(10**i))+(number%(10**i))
                if i <= 2 :
                    newNum += (number // 10**(i+1)) * (10**(i+1))
                if not visited[newNum] and isPrime(newNum):
                    visited[newNum] = 1
                    q.append((newNum,count+1))
    return "Impossible"

T = int(input().rstrip())
for _ in range(T):
    num1,num2 = map(int,input().split())
    visited = [0] * 10000
    print(bfs())
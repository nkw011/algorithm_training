import sys
from collections import deque
input = sys.stdin.readline

# PyPt3로 하니까 조금 빠르네...

def dfs(count,number):
    global n,minValue,maxValue,minStr,maxStr
    if count == n+1:
        value = 0
        for i in range(n):
            if inequality[i] == '<' and number[i] > number[i+1]:
                return
            elif inequality[i] == '>' and number[i] < number[i+1]:
                return
            value += number[i] * (10 **(n-i))
        value += number[n]
        result = "".join(map(str,number))
        
        minValue = min(minValue,value)
        if minValue == value:
            minStr = result
        
        maxValue = max(maxValue,value)
        if maxValue == value:
            maxStr = result 
        return
    
    for i in range(10):
        if not visited[i]:
            visited[i] = 1
            number.append(i)
            dfs(count+1,number)
            number.pop()
            visited[i] = 0
            
# DFS 성능개선 먼저 plunning을하기?
# 모든 경우의 수를 구하더라도 유효한 모든 경우의 수를 구하는 것이 시간 초과가 되지 않고 빠른 길이다.
def plunning(x,y,sign):
    if sign == '>' and x < y:
        return False
    elif sign == '<' and x > y :
        return False
    return True

def dfs2(count,number,value):
    global maxValue, minValue,minStr,maxStr
    if count == n+1:
        result = "".join(map(str,number))
        if minValue > value:
            minValue = value
            minStr = result
        if maxValue < value:
            maxValue = value
            maxStr = result
        return
    
    for i in range(10):
        if count == 0:
            number.append(i)
            visited[i] = 1
            dfs2(count+1,number,value + i * 10**(n-count))
            visited[i] = 0
            number.pop()
        elif count > 0 and not visited[i]:
            if plunning(number[count-1],i,inequality[count-1]):
                number.append(i)
                visited[i] = 1
                dfs2(count+1,number,value + i * 10**(n-count))
                visited[i] = 0
                number.pop()

n = int(input().rstrip())
inequality = list(input().split())
visited = [0] * (10)

minValue = 9876543211
maxValue = 0
minStr = ''
maxStr = ''

dfs2(0,deque(),0)
print(maxStr)
print(minStr)
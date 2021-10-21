import sys
input = sys.stdin.readline


result = 0

def dfs(numbers,n,count,target):
    global result
    if count == len(numbers)-1:
        if n + numbers[count] == target:
            result += 1 
        elif n - numbers[count] == target:
            result += 1
        return

    dfs(numbers,n+numbers[count],count+1,target)
    dfs(numbers,n-numbers[count],count+1,target)


def solution(numbers,target):
    dfs(numbers,0,0)
    return result
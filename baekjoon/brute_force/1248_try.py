import sys
input = sys.stdin.readline

n = int(input().rstrip())
inputs = list(input().rstrip())
sums = [[0] * n for _ in range(n)]
k = 0
result = []
for i in range(n):
    for j in range(i,n):
        sums[i][j] = inputs[k]
        k += 1

def promising(numbers,index):
    s = 0
    for i in range(index,-1,-1):
        s += numbers[i]
        if sums[i][index] == '0' and s != 0:
            return False
        if sums[i][index] == '-' and s >= 0:
            return False
        if sums[i][index] == '+' and s <= 0:
            return False
        
    return True
        
def dfs(numbers,count):
    global result
    
    if len(result) == n:
        return
    
    if count == n:
        result = numbers[:]
        return
    
    for i in range(-10,11):
        numbers.append(i)
        if promising(numbers,count):
            dfs(numbers,count+1)
        numbers.pop()
            
dfs([],0)
for number in result:
    print(number,end=" ")
print()
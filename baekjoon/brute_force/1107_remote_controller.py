import sys
input = sys.stdin.readline 

# for 문을 여러번 쓰는 것도 나쁘지 않은데?? ->총 6번만 하면 될듯
def dfs(number,lens,count,length):
    global channel,minValue
    if lens == length:
        count += abs(number-channel)
        minValue = min(minValue,count)
        return
    else :
        for i in range(10):
            if button[i] == 1 and visited1[i] < length:
                lens += 1
                number += i*(10**(length-lens))
                visited1 [i] +=1
                dfs(number,lens,count+1,length)
                number -= i*(10**(length-lens))
                lens -= 1
                visited1[i] -= 1


channelNum = list(map(int,input().rstrip()))
length = len(channelNum)
channel = 0
for i in range(length):
    channel += channelNum[i] * (10**(length -(i+1)))

num = int(input().rstrip())
button = [1] * 10
visited1 = [0] * 10
removed = list(map(int,input().split()))
for i in removed:
    button[i] = 0
    visited1[i] = length
minValue = 500000
dfs(0,0,0,length)

if length < 6:
    visited1 = [0] * 10
    for i in removed:
        button[i] = 0
        visited1[i] = length +1
    dfs(0,0,0,length+1)

if length > 1 :
    visited1 = [0] * 10
    for i in removed:
        button[i] = 0
        visited1[i] = length -1
    dfs(0,0,0,length-1)

minValue = min(minValue,abs(channel-100))
print(minValue)
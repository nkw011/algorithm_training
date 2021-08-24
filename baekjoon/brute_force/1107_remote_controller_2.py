import sys
input = sys.stdin.readline

channel = int(input().rstrip())
removeNum = int(input().rstrip())
removed = list(map(int,input().split()))
button = [1] * 10
for i in removed :
    button[i] = 0
        
minValue = 500000

# 000000 이 걸 제외 시켜야함... 즉 각 단계마다 0이 반복되는 현상을 지워야한다.
# 그냥 전체 1000000이렇게 해놓고 테스트 케이스 돌리는 게 가장 빠를듯
for a in range(10):
    number = 0
    if button[a] != 0:
        number += a 
        minValue = min(minValue,abs(number-channel) + 1)
    for b in range(10):
        if button[b] != 0:
            number += b * (10**1)
            minValue = min(minValue,abs(number-channel) + 2)
        for c in range(10):
            if button[c] != 0:
                number += c * (10**2)
                minValue = min(minValue,abs(number-channel) + 3)
            for d in range(10):
                if button[d] != 0:
                    number += d * (10**3)
                    minValue = min(minValue,abs(number-channel) + 4)
                for e in range(10):
                    if button[e] != 0:
                        number += e * (10**4)
                        minValue = min(minValue,abs(number-channel) + 5)
                    for f in range(10):
                        if button[f] != 0:
                            number += f * 10 **5
                            minValue = min(minValue,abs(number-channel) + 6)
minValue = min(minValue,abs(channel-100))
print(minValue)
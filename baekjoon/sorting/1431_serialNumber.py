import sys
input = sys.stdin.readline


################## 1안 - MergeSort를 활용한 풀이 ##############
# 런타임에러가 나오지만 그래도 합병정렬에대해 다시 알아간 계기였다.
n = int(input().rstrip())
serials = []
notIncludeNum =[]

def mergeSort(notIncludeNum,serials):
    leftI = 0
    rightI = 0
    result = []
    while leftI < len(notIncludeNum) and rightI < len(serials):
        if len(notIncludeNum[leftI]) < serials[rightI][0]:
            result.append(notIncludeNum[leftI])
            leftI += 1
        elif len(notIncludeNum[leftI]) > serials[rightI][0]:
            result.append(serials[rightI][2])
            rightI += 1
        else :
            for i in range(serials[rightI][0]):
                if ord(notIncludeNum[leftI][i]) < ord(serials[rightI][2][i]):
                    result.append(notIncludeNum[leftI])
                    leftI += 1
                    break
                elif ord(notIncludeNum[leftI][i]) > ord(serials[rightI][2][i]):
                    result.append(serials[rightI][2])
                    rightI += 1
                    break
    if leftI < len(notIncludeNum):
        for i in range(leftI,len(notIncludeNum)):
            result.append(notIncludeNum[i])
    else:
        for i in range(rightI,len(serials)):
            result.append(serials[i][2])
    return result

for i in range(n):
    serial = input().rstrip()
    countNum = 0
    findNum = False
    for j in range(len(serial)):
        if '0' <= serial[j] <= '9':
            findNum = True
            countNum += int(serial[j])
    if findNum:
        serials.append((len(serial),countNum,serial))
    else:
        notIncludeNum.append(serial)

notIncludeNum.sort()
serials = sorted(serials,key=lambda x : (x[0],x[1],x[2]))
result = mergeSort(notIncludeNum,serials)
for serial in result:
    print(serial)
#####################################################################################
# 괜히 뻘짓 하지말고 내가 아는 lambda나 잘 쓰자..
# lambda로 한게 오히려 올바른 풀이네... 조금 생각해볼까나.... 이게 왜 맞는지 이해된 정도가 거의 80%이긴하다...
# 근데 완벽히 이해된 것 같기도....??

for i in range(n):
    serial = input().rstrip()
    countNum = 0
    for j in range(len(serial)):
        if '0' <= serial[j] <= '9':
            countNum += int(serial[j])
    serials.append((len(serial),countNum,serial))
    
serials.sort(key=lambda x :(x[0],x[1],x[2]))
for serial in serials:
    print(serial[2])
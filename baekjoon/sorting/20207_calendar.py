# 각 날짜별로 일정 갯수만 만들면 되는 거잖아
# 예를 들어서 1일에 1개 2일에 2개 이런식으로 해서 계산하면 되네... 
# 다음 번에 이렇게 한 번 풀어봐야겠다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
calendar = []
table = []
plans = []
start = 366
end = 0
length = 0
for _ in range(n):
    s, e = map(int,input().split())
    if s < start:
        start = s
    if e > end :
        end = e
    plans.append((s,e))
    
plans = sorted(plans,key=lambda x:(x[0],-x[1]))

if n == 1:
    print(plans[0][1]-plans[0][0]+1)
else :
    for s,e in plans:
        if e > end:
            end = e
        possible = False
        for i in range(length):
            len1 = len(calendar[i])
            eDay = calendar[i][len1-1]
            if eDay+1== s:
                table[i][s:e+1] = [1] *(e-s+1)
                calendar[i][len1-1] = e
                possible = True
                break
            elif eDay+1 < s:
                calendar[i].append(s)
                calendar[i].append(e)
                table[i][s:e+1] = [1] *(e-s+1)
                possible = True
                break
        if not possible:
            calendar.append([s,e])
            table.append([0]*(end+2))
            length += 1
            table[length-1][s:e+1] = [1] *(e-s+1)
            
    startTable = length + 1
    endTable = -1
    startDay = end+1
    result = 0
    for day in range(start+1,end+2):
        possible = False
        for i in range(length):
            if table[i][day] == 1:
                if table[i][day-1] == 1:
                    startDay = min(startDay,day-1)
                else:
                    startDay = min(startDay,day)
                startTable = min(startTable,i)
                endTable = max(endTable,i)
                possible = True
            if table[i][day] == 0:
                if i == length-1 and not possible and startTable != length+1 and endTable != -1 and startDay != end +1:
                    result += (endTable-startTable+1) * (day-startDay)
                    startTable = length+1
                    endTable = -1
                    startDay = end+1
    print(result)
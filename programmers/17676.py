# 풀이: https://nkw011.github.io/programmers/programmers-17676/

from collections import defaultdict

####### 풀이2: 통과 ##############

# 1. 시간을 모두 ms 단위로 변경
# 2. 각 ms 당 몇 건의 log가 들어올 수 있는지 check
# 3. 메모리 초과가 일어나지 않은 이유는 각 log당 타임아웃이 3000이고 총 log수가 2000이기 때문에 dictionary key의 최대 갯수는 6000000이다.

def solution2(lines):
    count = defaultdict(int)
    for line in lines:
        _, t, interval = line.split()
        h, m, s = t.split(":")
        end_time = int(float(h) * 60 * 60 * 1000 + float(m) * 60 * 1000 + float(s) * 1000)
        interval = int(float(interval[:-1]) * 1000)
        for t in range(end_time-interval+1, end_time+1):
            count[t] += 1
        for t in range(end_time+1, end_time+1000):
            count[t] += 1
    return max(count.values())

######### 풀이1: 시간초과 ###########

def make_time_logs(lines):
    logs = []
    for line in lines:
        _, t, interval = line.split()
        h, m, s = t.split(":")
        end_time = float(h) * 60 * 60 * 1000 + float(m) * 60 * 1000 + float(s) * 1000
        interval = float(interval[:-1]) * 1000
        logs.append((int(end_time - interval + 1), int(end_time)))
    return logs

def solution(lines):
    logs = make_time_logs(lines)
    max_cnt = 1
    for i, (s1, e1) in enumerate(logs):
        for t in range(s1, e1+1):
            cnt = 1
            for s2,e2 in logs[i+1:]:
                if t <= s2 < t +1000:
                    cnt += 1
                elif t <= e2 < t +1000:
                    cnt +=1
            if max_cnt < cnt:
                max_cnt = cnt
    return max_cnt


if __name__ == '__main__':
    lines = [
            "2016-09-15 01:00:04.001 2.0s",
            "2016-09-15 01:00:07.000 2s"
             ]
    print(solution2(lines))

# https://programmers.co.kr/learn/courses/30/lessons/17678

# 결론: 가장 마지막에 인원이 남는지 없는지 체크해서 남으면 마지막에 타고, 남지않으면 m번째 사람보다 일찍 오기

from bisect import bisect_left


def time_to_minute(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


def time_to_str(t):
    h, m = str(t // 60), str(t % 60)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    return h + ":"+m


def solution(n, t, m, timetable):
    timetable = list(map(time_to_minute, timetable))
    timetable.sort()
    # 이것때문에 마지막 버스를 탈 수 없는 사람은 아예 제외가 된다. 따라서 그냥 m번째 사람보다 일찍 오면 된다.
    timetable = [tm for tm in timetable if tm < 9*60+(n * t)]
    ret = -1
    for i, tm in enumerate(range(60*9, 60*9+t*n, t)):
        if i == n-1:
            if len(timetable) < m:
                ret = tm
            else:
                ret = timetable[m-1]-1
        else:
            idx = bisect_right(timetable, tm)
            if idx < m:
                timetable = timetable[idx:]
            else:
                timetable = timetable[m:]
    return time_to_str(ret)

# 해설: https://nkw011.github.io/programmers/programmers-72414/

def str2time(time_string):
    h,m,s = time_string.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def time2str(time_number):
    h,m,s = (time_number // 3600), (time_number % 3600 // 60), (time_number % 3600 % 60)
    h = str(h) if len(str(h)) == 2 else '0' + str(h)
    m = str(m) if len(str(m)) == 2 else '0' + str(m)
    s = str(s) if len(str(s)) == 2 else '0' + str(s)
    return ":".join([h, m, s])


def solution(play_time, adv_time, logs):
    play_t, adv_t = str2time(play_time), str2time(adv_time)

    if play_t == adv_t: return '00:00:00'

    record = [0] * (play_t+1)
    for log in logs:
        start_time, end_time = log.split("-")
        start_t, end_t = str2time(start_time), str2time(end_time)
        record[start_t] += 1
        record[end_t] -= 1

    for _ in range(2):
        for i in range(1, play_t+1):
            record[i] += record[i-1]

    start_t, max_t = 0,record[adv_t-1]
    for i in range(adv_t+1,play_t+1):
        temp = record[i-1] - record[i-adv_t-1]
        if temp > max_t:
            start_t,max_t = i-adv_t, temp

    return time2str(start_t)


if __name__ == '__main__':
    play_time, adv_time = "50:00:00", "50:00:00"
    logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    print(solution(play_time, adv_time, logs))

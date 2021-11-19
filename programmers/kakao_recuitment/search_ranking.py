# https://programmers.co.kr/learn/courses/30/lessons/72412

from bisect import bisect_left


def initTotalData():
    data = {}
    for k1 in ["java", "cpp", "python", "-"]:
        for k2 in ["backend", "frontend", "-"]:
            for k3 in ["junior", "senior", "-"]:
                for k4 in ["pizza", "chicken", "-"]:
                    data[(k1, k2, k3, k4)] = []
    return data


def makeTotalData(total_data, infos):
    new_data = total_data
    for info in infos:
        inf = info.split(" ")
        for k1 in [inf[0], "-"]:
            for k2 in [inf[1], "-"]:
                for k3 in [inf[2], "-"]:
                    for k4 in [inf[3], "-"]:
                        total_data[(k1, k2, k3, k4)].append(int(inf[4]))
    for k in new_data.keys():
        new_data[k].sort()
    return new_data

# 데이터를 처음부터 끝까지 찾으려면 50000 * 100000이 걸리기 때문에 이분 탐색이 필요한 케이스였다.
# 이런 문제가 query형 문제였다니... 이제 처음 알았다.


def solution(info, query):
    ret = []
    total_data = initTotalData()
    total_data = makeTotalData(total_data, info)

    for q in query:
        cond = q.split(" ")
        data = total_data[(cond[0], cond[2], cond[4], cond[6])]
        result = len(data) - bisect_left(data, int(cond[7]))
        ret.append(result)
    return ret

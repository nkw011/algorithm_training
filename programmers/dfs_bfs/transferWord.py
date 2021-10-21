# https://programmers.co.kr/learn/courses/30/lessons/43163

INF = 10000


def solution(begin, target, words):
    words.insert(0, begin)
    leng = len(words)
    lenStr = len(begin)
    e = -1
    count = [[INF] * (leng) for _ in range(leng)]
    for i in range(leng):
        if words[i] == target:
            e = i
        for j in range(i+1, leng):
            cnt = 0
            for idx in range(lenStr):
                if words[i][idx] != words[j][idx]:
                    cnt += 1
            if cnt <= 1:
                count[i][j] = 1
                count[j][i] = 1
    if e == -1:
        return 0
    for k in range(leng):
        for i in range(leng):
            for j in range(leng):
                count[i][j] = min(count[i][j], count[i][k] + count[k][j])
    return count[0][e]

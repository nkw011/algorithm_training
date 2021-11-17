# https://programmers.co.kr/learn/courses/30/lessons/81302

def manhatten(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def check_partition(place, p1, p2):
    if p1[0] == p2[0] and place[p1[0]][max(p1[1], p2[1]) - 1] == 'X':
        return 1
    if p1[1] == p2[1] and place[max(p1[0], p2[0])-1][p1[1]] == 'X':
        return 1
    if abs(p1[0] - p2[0]) == abs(p1[1]-p2[1]) == 1:
        if place[p1[0]][p2[1]] == 'X' and place[p2[0]][p1[1]] == 'X':
            return 1
    return 0


def solution(places):
    result = [1] * 5
    for idx, place in enumerate(places):
        person = [(i, j) for i, arr in enumerate(place)
                  for j, c in enumerate(arr) if c == 'P']
        total = len(person)
        notChecked = [(i, j) for i in range(total) for j in range(
            i+1, total) if manhatten(person[i], person[j]) <= 2]
        for i, j in notChecked:
            result[idx] = min(result[idx], check_partition(
                place, person[i], person[j]))
    return result

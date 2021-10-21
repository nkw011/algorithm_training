# https://programmers.co.kr/learn/courses/30/lessons/43164

answer = []


def dfs(now, cnt, total, tickets, visited, path):
    global answer
    if cnt == total:
        answer = path[:]
        return True
    for idx, t in enumerate(tickets):
        if not visited[idx] and t[0] == now:
            visited[idx] = 1
            path.append(t[1])
            if dfs(t[1], cnt+1, total, tickets, visited, path):
                return True
            path.pop()
            visited[idx] = 0


def solution(tickets):
    total = len(tickets)
    visited = [0] * (total)
    tickets.sort(key=lambda x: (x[0], x[1]))
    for idx, ticket in enumerate(tickets):
        if ticket[0] == 'ICN':
            visited[idx] = 1
            if dfs(ticket[1], 1, total, tickets, visited, ["ICN", ticket[1]]):
                return answer
            visited[idx] = 0

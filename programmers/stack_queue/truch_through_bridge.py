# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = [[bridge_length+1,0]]
    now_br_weight,now_br_num = 0,1
    while bridge:
        answer += 1
        i = -1
        for idx,(t,c) in enumerate(bridge):
            if t+1 > bridge_length:
                now_br_num -= 1
                now_br_weight -= c
                i = idx
            bridge[idx][0] = t+1
        if i != -1: 
            bridge = bridge[i+1:]
        if truck_weights: 
            w = truck_weights[0]
            if now_br_num +1 <= bridge_length and now_br_weight + w <= weight:
                truck_weights.popleft()
                now_br_num += 1
                now_br_weight += w
                bridge.append([1,w])
    return answer

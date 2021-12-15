# https://programmers.co.kr/learn/courses/30/lessons/49993
# 아예 거꾸로 확인해서 전 문자가 존재하고 현재 idx가 제대로 되어있는지 확인

def solution(skill, skill_trees):
    skill_dict = [{s:idx for idx,s in enumerate(s_t)} for s_t in skill_trees]
    cnt,leng = 0, len(skill)
    for d in skill_dict:
        possible = True
        for i in range(leng-1,0,-1):
            if skill[i] in d.keys():
                if skill[i-1] not in d.keys() or d[skill[i-1]] > d[skill[i]]:
                    possible = False
                    break
        if possible:
            cnt += 1
    return cnt

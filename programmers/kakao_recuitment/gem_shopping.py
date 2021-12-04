# https://programmers.co.kr/learn/courses/30/lessons/67258

# 왜 효율성 테스트에서 떨어졌나?
# 1. 모든 보석들이 있는지 확인하기 위해 매번마다 set을 만들어서 갯수를 체크하였기 때문이다.

# 결론
# 1. 어차피 two pointer를 이용하기 때문에 갯수를 1개씩 셀 수 있다. -> 따라서 매번마다 set을 구해서 길이를 구할 필요가 없다.
# 2. 갯수를 세는 것은 dictionary를 이용하였다.

from collections import defaultdict

def solution(gems):
    s,e = -1,-1
    l,r,leng,total = 0, 1, len(gems), len(set(gems))
    gem_dict = defaultdict(int)
    gem_dict[gems[l]] += 1
    while l < r and r <= leng:
        if len(gem_dict) < total:
            if r < leng: gem_dict[gems[r]] += 1
            r+= 1
        else:
            if s == -1 or (e-s) > (r-l):
                s,e = l,r
            gem_dict[gems[l]] -= 1
            if gem_dict[gems[l]] == 0:
                del gem_dict[gems[l]]
            l += 1
    return [s+1,e]

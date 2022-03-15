# 단어마다 알파벳이 몇 개 존재하는 지 체크
# 퍼즐마다 알파벳이 몇 개 존재하는 지 체크한 이후 각 알파벳 별로 중앙에 들어왔을 때 몇 개의 단어가 존재할 지 체크한 이후 출력하기
import sys
from collections import Counter
def input(): return sys.stdin.readline().rstrip()


words = []
puzzles = []
isPuzzle = 0

while True:
    w = input()
    if w == '-':
        isPuzzle = True
        continue
    if w == '#':
        break

    if isPuzzle:
        puzzles.append(Counter(w))
    else:
        words.append(Counter(w))

for puzzle in puzzles:
    indices = []
    cnts = {k: 0 for k in puzzle.keys()}

    for word in words:
        possible = True
        for w in word.keys():
            if w not in puzzle.keys() or word[w] > puzzle[w]:
                possible = False
        if possible:
            for k in cnts:
                if k in word.keys():
                    cnts[k] += 1

    min_cnt, max_cnt = min(cnts.values()), max(cnts.values())
    max_ws, min_ws = sorted([k for k in cnts if cnts[k] == max_cnt]), sorted(
        [k for k in cnts if cnts[k] == min_cnt])

    print("".join(min_ws), min_cnt, "".join(max_ws), max_cnt)

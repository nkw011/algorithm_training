# 풀이 및 해설: https://nkw011.github.io/baekjoon/baekjoon-1254/

import sys
def input(): return sys.stdin.readline().rstrip()

def is_palinedrome(s):
    length = len(s)
    for i in range(length//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

s = input()
length = len(s)
for i in range(length+1):
    if is_palinedrome(s+s[:i][::-1]):
        print(len(s+s[:i][::-1]))
        break

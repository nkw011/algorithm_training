import sys
import re
def input(): return sys.stdin.readline().rstrip()

reg = re.compile('(100+1+|01)+')

for _ in range(int(input())):
    if re.fullmatch(reg,input()):
        print("YES")
    else:
        print("NO")

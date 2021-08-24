import sys
input = sys.stdin.readline

exp = input().rstrip()
exp2 = exp
if exp2.find("+") != -1:
    exp2 = exp2.replace("+"," ")
if exp2.find("-") != -1:
    exp2 = exp2.replace("-", " ")
exp2 = list(map(int,exp2.split()))
exp3 = []

findNum = False
i = 0
for val in exp:
    if val not in ['+','-']:
        if not findNum:
            exp3.append(str(exp2[i]))
            i += 1
            findNum = True
    else:
        exp3.append(val)
        findNum = False

exp = "".join(exp3)
exp2 = []
open = False
for val in exp:
    if val == '-':
        if open:
            exp2.append(')')
        exp2.append('-')
        exp2.append('(')
        open = True
    else :
        exp2.append(val)
if open :
    exp2.append(')')

exp3 = "".join(exp2)
print(eval(exp3))
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
for _ in range(n):
    m = int(input())
    numbers = list([input() for _ in range(m)])
    numbers.sort()
    possible = True
    for i, num in enumerate(numbers[:-1]):
        if num == numbers[i+1][:len(num)]:
            possible = False
            break
    if possible:
        print('YES')
    else:
        print('NO')

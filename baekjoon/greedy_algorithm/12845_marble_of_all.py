import sys
input = sys.stdin.readline

n = int(input().rstrip())
cards = list(map(int,input().split()))
cards.sort(reverse=True)
gold = 0
for i in range(1,n):
    gold += (cards[0] + cards[i])
print(gold)
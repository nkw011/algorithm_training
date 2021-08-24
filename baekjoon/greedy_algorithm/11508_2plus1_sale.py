import sys
input = sys.stdin.readline

n = int(input().rstrip())
product = [int(input().rstrip()) for _ in range(n)]
product.sort(reverse=True)

if n < 3:
    print(sum(product))
else:
    discount = 0
    for i in range(2,n,3):
        discount += product[i]
    print(sum(product) - discount)
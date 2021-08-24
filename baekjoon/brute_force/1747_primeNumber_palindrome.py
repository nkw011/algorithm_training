import sys, math
input = sys.stdin.readline

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    limit = int(math.sqrt(num)) +1
    for i in range(2,limit):
        if num % i == 0:
            return False
    return True

def palindrome(number):
    length = len(number)
    for i in range(length//2):
        if number[i] != number[length-1-i]:
            return False
    return True

number = int(input().rstrip())
while True:
    if isPrime(number) and palindrome(str(number)):
        print(number)
        break
    number += 1
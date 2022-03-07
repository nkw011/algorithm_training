import sys
from collections import Counter
def input(): return sys.stdin.readline().rstrip()

def transpose(arr):
    n, m = len(arr), len(arr[0])
    new_arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_arr[j][i] = arr[i][j]
    return new_arr

def command(array, is_row):
    arr_n, arr_m = len(array), len(array[0])
    n = arr_n if is_row else arr_m
    m = arr_m if is_row else arr_n
    new_arr = []
    for i in range(n):
        arr = []
        for j in range(m):
            if is_row:
                arr.append(array[i][j])
            else:
                arr.append(array[j][i])
        counter = Counter(arr)
        temp = sorted(list(counter.items()), key=lambda x: (x[1], x[0]))
        arr_temp = []
        for k, v in temp:
            if k == 0:
                continue
            arr_temp.append(k)
            arr_temp.append(v)
        new_arr.append(arr_temp)
    max_length = max(list(map(len, new_arr)))
    ret_arr = []
    for arr in new_arr:
        length = len(arr)
        temp = arr
        if length != max_length:
            temp = arr + [0] * (max_length - length)
        ret_arr.append(temp[:100])
    if is_row:
        return ret_arr
    return transpose(ret_arr)

def main():
    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]

    for cnt in range(101):
        row, col = len(A), len(A[0])
        if r-1 < row and c-1 < col and A[r-1][c-1] == k:
            return cnt
        is_row = 1 if row >= col else 0
        A = command(A, is_row)
    return -1

print(main())

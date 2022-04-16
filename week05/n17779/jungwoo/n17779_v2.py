from sys import stdin

input1 = stdin.readline
# directions = (
#     (-1, 0),  # 상
#     (0, -1),  # 좌
#     (1, 0),  # 하
#     (0, 1),  # 우
# )


# def is_in_range(obj, a, b):
#     if isinstance(obj, int):
#         return 0 <= a < obj and 0 <= b < obj
#     else:
#         return 0 <= a < len(obj) and 0 <= b < len(obj)


def search_rc(total, n, arr, x, y, d1, d2):
    cnt = [0] * 5
    a1, b1 = x, y
    a2, b2 = a1 + d1, b1 - d1
    a3, b3 = a2 + d2, b2 + d2
    a4, b4 = a3 - d1, b3 + d1
    for i in range(n):
        if i < a1:
            cnt[1] += arr[i][b1]
            cnt[2] += arr[i][-1] - arr[i][b1]
        elif a1 <= i < min(a2, a4):
            diff = i - a1
            cnt[1] += arr[i][b1 - diff - 1]
            cnt[2] += arr[i][-1] - arr[i][b1 + diff]
        elif max(a2, a4) < i <= a3:
            diff = a3 - i
            cnt[3] += arr[i][b3 - diff - 1]
            cnt[4] += arr[i][-1] - arr[i][b3 + diff]
        elif a3 < i:
            cnt[3] += arr[i][b3 - 1]
            cnt[4] += arr[i][-1] - arr[i][b3 - 1]
        else:
            if i < a2:
                diff = i - a1
                cnt[1] += arr[i][b1 - diff - 1]
            elif a2 == i:
                cnt[3] += arr[i][b2 - 1]
            else:
                diff = i - a2
                cnt[3] += arr[i][b2 + diff - 1]
            if i <= a4:
                diff = i - a1
                cnt[2] += arr[i][-1] - arr[i][b1 + diff]
            else:
                diff = i - a4
                cnt[4] += arr[i][-1] - arr[i][b4 - diff]
    cnt[0] = total - sum(cnt)
    return cnt


def search_d1d2(total, n, arr, x, y):
    min_diff = 2000
    for d1 in range(1, min(n - x - 1, y)):
        for d2 in range(1, min(n - y - 1, n - x - d1)):
            cnt = search_rc(total, n, arr, x, y, d1, d2)
            min_diff = min(max(cnt) - min(cnt), min_diff)
    return min_diff


def search_xy(total, n, arr):
    min_diff = 2000
    for i in range(1, n - 2):
        for j in range(1, n - 2):
            min_diff = min(search_d1d2(total, n, arr, i, j), min_diff)
    return min_diff


def init(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            arr[i][j] += arr[i][j-1]
        total += arr[i][-1]
    return total


def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = init(arr)
    print(search_xy(total, n, arr))


if __name__ == "__main__":
    solution()

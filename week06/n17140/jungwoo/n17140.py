from collections import defaultdict
from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),  # 우
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
)


def is_in_range(obj, a, b):
    if isinstance(obj, int):
        return 0 <= a < obj and 0 <= b < obj
    else:
        return 0 <= a < len(obj) and 0 <= b < len(obj)


def init(arr):
    for i in range(3):
        tmp = list(map(int, input().split()))
        for j in range(3):
            arr[i][j] = tmp[j]


def my_sort(arr, range1, range2):
    dic = defaultdict(int)
    for i in range1:
        for j in range2:
            if arr[i][j] != 0:
                dic[arr[i][j]] += 1
    sorted_dic = sorted(list(map(list, dic.items())), key=lambda _x: (_x[1], _x[0]))
    return sum(sorted_dic, [])


def r_func(arr, r, clen):
    return my_sort(arr, range(r, r + 1), range(clen))


def c_func(arr, rlen, c):
    return my_sort(arr, range(rlen), range(c, c + 1))


def r_allocate(arr, r, clen, new_partial):
    for i in range(min(len(new_partial), 100)):
        arr[r][i] = new_partial[i]
    for i in range(min(len(new_partial), 100), min(100, max(len(new_partial), clen))):
        arr[r][i] = 0


def c_allocate(arr, rlen, c, new_partial):
    for i in range(min(len(new_partial), 100)):
        arr[i][c] = new_partial[i]
    for i in range(min(len(new_partial), 100), min(100, max(len(new_partial), rlen))):
        arr[i][c] = 0


def solution():
    r, c, k = map(int, input().split())
    arr = [[0] * 100 for _ in range(100)]

    init(arr)

    rlen, clen, cnt = 3, 3, 0
    while arr[r-1][c-1] != k and cnt <= 100:
        if rlen >= clen:
            new_clen = 0
            for i in range(rlen):
                new_partial = r_func(arr, i, clen)
                r_allocate(arr, i, clen, new_partial)
                new_clen = max(new_clen, len(new_partial))
            clen = new_clen
        else:
            new_rlen = 0
            for i in range(clen):
                new_partial = c_func(arr, rlen, i)
                c_allocate(arr, rlen, i, new_partial)
                new_rlen = max(new_rlen, len(new_partial))
            rlen = new_rlen
        cnt += 1
    print(cnt if arr[r-1][c-1] == k else -1)


if __name__ == "__main__":
    solution()


# 배열 인덱스 1부터 시작
# 1초 지난 때마다 !!!연산!!!
#     R연산: 행에 대해 정렬. 행이 더 많거나 같을 때
#     C연산: 반대
#
# 정렬하는 방법
# 행, 열 쭉 긁어서 각 수가 몇 번 나왔는지 알아야 함
# 등장 횟수 오름차순, 숫자 오름차순
#
# 정렬 결과 넣는 방법
# 수와 등장 횟수 모두 넣음
# 수가 먼저
# [3,1,1]
# [3,1, 1,2]
# [2,1, 3,1, 1,2]
#
# 정렬은 마지막 행, 열에만
# 정렬시 빈 공간은 0으로 채움
# 정렬시 0은 무시
#
# 행, 열 길이 100 이상이면 버림림
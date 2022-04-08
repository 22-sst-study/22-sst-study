from collections import deque

# input = stdin.readline

# directions = (
#     (-1, 0),  # 상
#     (0, -1),  # 좌
#     (1, 0),  # 하
#     (0, 1),  # 우
# )


# def is_in_range(n, a, b):
#     return 0 <= a < n and 0 <= b < n


def move(arr, n):
    def _check_if_last_on():
        if arr[n - 1][1]:
            arr[n - 1][1] = 0
    _check_if_last_on()
    new_empty_cnt = 0
    for i in range(n - 2, 0, -1):
        if arr[i][1] == 1 and arr[i + 1][1] == 0 and arr[i + 1][0] > 0:
            arr[i][1], arr[i + 1] = 0, [arr[i + 1][0] - 1, 1]
            if arr[i + 1][0] == 0:
                new_empty_cnt += 1
    _check_if_last_on()
    return new_empty_cnt


def robot_on(arr):
    if arr[0][0] > 0:
        arr[0] = [arr[0][0] - 1, 1]
        if arr[0][0] == 0:
            return 1
    return 0


def solution():
    n, k = map(int, input().split())
    arr = deque(list(map(lambda _x: [int(_x), 0], input().split())))  # [duration, robot_on or robot_off]

    cnt, empty_count = 1, 0
    while True:
        # rotate
        arr.rotate(1)

        # move robot
        empty_count += move(arr, n)

        # robot on
        empty_count += robot_on(arr)

        # count empty
        if empty_count >= k:
            break

        cnt += 1

    print(cnt)


if __name__ == "__main__":
    solution()

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


def dragon(dot, dot_set, r, c, d, g, prev):  # prev: 이전 턴에서 진행했던 방향 배열을 역순으로 뒤집고 -를 붙인 것(방향을 반대로 함)
    if g == 0:
        return
    cr, cc, cd = r, c, d
    turnned_prev = [1] + prev  # prev에 시계 방향 90도 회전을 더한 것. 즉, 이번 턴에서 그려야 할 드래곤 커브의 방향 배열
    for pd in turnned_prev:  # 드래곤 커브 그리기
        x, y = directions[(cd + pd) % 4][0] + cr, directions[(cd + pd) % 4][1] + cc
        dot[x][y] = 1
        dot_set.add((x, y))
        cr, cc, cd = x, y, (cd + pd) % 4
    curr_reverse = [-turnned_prev[len(turnned_prev)-i-1] for i in range(len(turnned_prev))]  # 다음 턴의 커브를 그리기 위해 이번 턴에서 사용했던 방향 배열을 역순으로 뒤집고 -를 붙임
    next_turns = curr_reverse + prev  # 이전 턴의 드래곤 커브와 현재 턴의 드래곤 커브를 합쳐서 다음 턴의 드래곤 커브 방향 배열을 만듦
    dragon(dot, dot_set, cr, cc, cd, g - 1, next_turns)


def search(dot, dot_set):
    square = 0
    for r, c in dot_set:
        tmp = (r, c), (r, c+1), (r+1, c), (r+1, c+1)
        if all([is_in_range(len(dot), t[0], t[1]) and dot[t[0]][t[1]] for t in tmp]):
            square += 1
    return square


def solution():
    n = int(input())

    dot = [[0] * 101 for _ in range(101)]
    dot_set = set()

    for _ in range(n):
        c, r, d, g = map(int, input().split())
        x, y = directions[d][0] + r, directions[d][1] + c
        dot[r][c] = dot[x][y] = 1
        dot_set |= {(r, c), (x, y)}
        dragon(dot, dot_set, x, y, d, g, [])

    print(search(dot, dot_set))


if __name__ == "__main__":
    solution()

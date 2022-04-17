from collections import deque

# 16234 인구이동
# 2022-04-17 07:28~08:30
# python3 시간초과 pypy3 1340ms

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
day = 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]
    peo = board[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and L <= abs(board[nx][ny] - board[x][y]) <= R and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                union.append((nx, ny))
                peo += board[nx][ny]
                cnt += 1

    for i, j in union:
        board[i][j] = peo // cnt

    return len(union)


while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True

    if not flag:
        break

    day += 1

print(day)

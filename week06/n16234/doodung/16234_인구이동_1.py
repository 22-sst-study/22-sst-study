from collections import deque

# 16234 인구이동
# python3 시간초과 pypy3 1340ms
# bfs
# 어려웠던 점 : 인구 이동이 없을 경우 종료 조건
# 시간 줄일 방법은 ????

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
day = 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]  # 연합
    peo = board[x][y]  # 인구수
    cnt = 1  # 연합된 국가 수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인구 차이가 L명 이상 R명 이하라면, 연합 국가에 넣기
            if 0 <= nx < N and 0 <= ny < N and L <= abs(board[nx][ny] - board[x][y]) <= R and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                union.append((nx, ny))
                peo += board[nx][ny]
                cnt += 1

    # 연합을 이루고 있는 각 칸의 인구수
    for i, j in union:
        board[i][j] = peo // cnt

    return len(union)


# 인구 이동 없을 때까지 반복
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True

    # 지금까지 인구 이동 없을 경우 그만하기
    if not flag:
        break

    day += 1

print(day)

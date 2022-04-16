from collections import deque
import sys
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 0은 빈 칸  /  1은 벽  /  2는 바이러스의 위치
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(virus):
    result = 0
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    for x, y in virus:
        queue.append((x, y, 0))
    while queue:
        x, y, time = queue.popleft()
        if visited[x][y] :
            continue
        else:
            visited[x][y] = time
            for i in range(4):
                nx, ny = x + directions[i][0], y + directions[i][1]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] != 1:
                    queue.append((nx, ny, time+1))
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 :
                if visited[i][j] == 0 : return INF  
                result = max(result, visited[i][j])
    return result

virusLoc = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virusLoc.append((i, j))

answer = INF
## combinations 활용
for virus in combinations(virusLoc, M):
    answer = min(answer, bfs(virus))

## 백트래킹 활용
# def btr(loc, dep, arr):
#     global answer
#     if dep == M:
#         answer = min(answer, bfs(arr)) ## arr가 M만큼 채워지면 bfs실행
#         return
#     if loc >= len(virusLoc):
#         return
#     for i in range(loc, len(virusLoc)):
#         arr.append(virusLoc[i])
#         btr(i+1, dep+1, arr)
#         arr.pop()
# btr(0, 0, [])

if answer == INF:
    print(-1)
else: 
    print(answer)
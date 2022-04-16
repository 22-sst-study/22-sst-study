'''
pypy3: 228ms
python3: 376ms
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(N)]
turns = [list(map(int, input().split())) for _ in range(T)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def BFS():
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    num = 0 # 인접하면서 같은 수(그룹) 의 갯수
    for i in range(N):
        for j in range(M):
            tmp = []
            if arr[i][j] == 0 : continue
            if visited[i][j] == 0 : 
                queue.append((i, j))
                visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                tmp.append((x, y))
                for n in range(4):
                    nx, ny = x + directions[n][0], (y + directions[n][1])%M
                    if 0<=nx<N and arr[nx][ny] == arr[i][j] and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
            if len(tmp) >1:
                num += 1
                for x, y in tmp:
                    arr[x][y] = 0   
    if num == 0:
        _tmp = {}
        _sum = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] >0: 
                    _tmp[(i, j)] = arr[i][j]
                    _sum += arr[i][j]
        if len(_tmp) > 0: ## 예외처리 !
            avg = _sum / len(_tmp)
            for (x, y), v in _tmp.items():
                if v > avg:
                    arr[x][y] -= 1
                elif v < avg : 
                    arr[x][y] += 1

for line, direc, num in turns:
    ''' 원판 돌리기 '''
    if direc == 0 : direc = 1
    elif direc == 1 : direc = -1
    nline = line
    while nline <= N:
        for _ in range(num):
            arr[nline-1].rotate(direc)
        nline += line
    BFS()

answer = 0 
for a in arr:
    answer += sum(a)
print(answer)
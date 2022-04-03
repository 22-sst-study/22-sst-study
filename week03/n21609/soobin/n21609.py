import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M = list(map(int, input().split()))
arr =  [list(map(int, input().split())) for _ in range(N)]
answer = 0

def gravity(arr):
    for i in range(N-2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if arr[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<N and arr[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        arr[r+1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else:
                        break
def rotate(arr):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[N-1-j][i] = arr[i][j]
    return temp

while True:
    blockGroup = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 :
                visited = [[0] * N for _ in range(N)]
                curNode = arr[i][j] ## 현재 일반 블록 색깔
                queue = deque([(i, j)])
                visited[i][j] = 1
                block_cnt, rainbow_cnt = 1, 0  # 블록개수, 무지개블록 개수
                blocks, rainbows = [(i, j)], []  # 블록좌표 넣을 리스트, 무지개좌표 넣을 리스트  
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == curNode: ## 일반블록
                            visited[nx][ny] = 1
                            queue.append((nx, ny))
                            block_cnt += 1
                            blocks.append((nx, ny))
                        elif 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == 0: ## 무지개블록
                            visited[nx][ny] = 1
                            queue.append((nx, ny))
                            block_cnt += 1
                            rainbow_cnt += 1
                            rainbows.append((nx, ny))
                for x,y in rainbows:
                    visited[x][y] = 0
                if block_cnt >= 2:
                    blockGroup.append([block_cnt, rainbow_cnt, blocks + rainbows])

    blockGroup.sort(reverse = True)     
    if not blockGroup:
        break
    answer += blockGroup[0][0] ** 2
    for x, y in blockGroup[0][2]:
        arr[x][y] = -2
    gravity(arr)
    arr = rotate(arr)
    gravity(arr)

print(answer)


'''
PyPy3 : 220ms
python : 364ms
'''

import sys
input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 위, 아래, 왼쪽, 오른쪽

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction_tmp = list(map(int, input().split()))
sharkPriority = [[] for _ in range(M)]
for i in range(M):
    for _ in range(4):
        sharkPriority[i].append(list(map(int, input().split())))

smell = [[[0, 0] for _ in range(N)] for _ in range(N)] # [상어인덱스, 남은횟수]
sharks = [[] for _ in range(M)] # [상어 방향, x좌표, y좌표]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 :
            shark = arr[i][j]-1
            sharks[shark] = [direction_tmp[shark]-1, i, j]
            smell[i][j] = [shark, K]

def decreaseSmell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] >0:
                smell[i][j][1] -= 1
            if smell[i][j][1] ==0:
                smell[i][j] = [0, 0]

def move():
    global outNum
    tmp = {} #상어가 이동할 곳 임시 저장
    for idx, shark in enumerate(sharks):
        direct, x, y = shark
        if x == -1:
            continue
        else:
            priority = sharkPriority[idx][direct]
            newX, newY, newDirect = -1, -1, -1
            mine = (-1, -1, -1)
            for n in priority:
                nx = x + direction[n-1][0]
                ny = y + direction[n-1][1]
                if 0<=nx<N and 0<=ny<N:
                    if smell[nx][ny][1] == 0:
                        newX, newY = nx, ny
                        newDirect = n-1
                        break
                    elif smell[nx][ny][0] == idx and mine == (-1, -1,-1):
                        mine = (nx, ny, n-1)
            if newX == newY == -1:
                newX, newY, newDirect = mine

            if (newX, newY) in tmp:
                n_idx = tmp[(newX, newY)][0] 
                if n_idx < idx: ## 안바꾸는경우
                    sharks[idx] = [-1, -1, -1]
                    outNum += 1
                    continue
                else: ## 바꾸는 경우
                    sharks[n_idx] = [-1, -1, -1]
                    outNum += 1
            tmp[(newX, newY)] = [idx, newDirect] 
    ## tmp에서 실제 배열로 반영
    for key, value in tmp.items():
        x, y = key
        smell[x][y] = [value[0], K+1]
        sharks[value[0]] = [value[1], x, y]

answer = 0
outNum = 0
while True:
    answer += 1
    if answer > 1000: 
        print(-1)
        break
    move()
    decreaseSmell()
    if outNum == M-1:
        print(answer)
        break

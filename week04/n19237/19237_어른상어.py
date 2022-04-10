# 19237 어른상어
# 29200KB, 760MS

# N : 격자 크기, M : 상어가 들어있는 칸의 개수, K : 냄새 지속 기간
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = list(map(int, input().split()))
print(dir)
# 상어들의 우선순위 : 위,아래,왼쪽,오른쪽 향할 때 우선순위
shark_priority = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        shark_priority[i].append(list(map(int, input().split())))

print(shark_priority)
# 냄새 리스트[상어번호, 냄새 지속 기간]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

while True:
    # 모든 상어가 자신의 위치에 냄새를 뿌린다.
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0: # 냄새 뿌림
                smell[i][j][1] -= 1
            if board[i][j] != 0:  # 상어가 있으면
                smell[i][j] = [board[i][j], K]  # 상어 냄새, 냄새 지속 기간 저장

    # 그 후 1초마다 모든 상어가 이동하고 자신의 냄새를 그 칸에 뿌림
    temp = [[0 for _ in range(N)] for _ in range(N)]

    # 아무 냄새가 없는 칸을 찾는 과정
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                now_dir = dir[board[x][y] - 1]
                print(now_dir)
                found = False
                for z in range(4):
                    nx = x + dx[shark_priority[board[x][y] - 1][now_dir - 1][z] - 1]
                    ny = y + dy[shark_priority[board[x][y] - 1][now_dir - 1][z] - 1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][1] == 0:  # 아무 냄새가 없을 경우
                            dir[board[x][y] - 1] = shark_priority[board[x][y] - 1][now_dir - 1][z]
                            if temp[nx][ny] == 0:
                                temp[nx][ny] = board[x][y]
                            else:
                                temp[nx][ny] = min(temp[nx][ny], board[x][y])
                            found = True
                            break

                # 위에서 칸을 찾았는지 안찾았는지 체크하는 단계
                if found:
                    continue

                # 모든 칸에 냄새가 차있어서 위에서 움직이지 못했을 경우
                # 이제 자신의 냄새가 있는 칸을 찾는 단계
                for me in range(4):
                    nx = x + dx[shark_priority[board[x][y] - 1][now_dir - 1][me] - 1]
                    ny = y + dy[shark_priority[board[x][y] - 1][now_dir - 1][me] - 1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][0] == board[x][y]:
                            dir[board[x][y] - 1] = shark_priority[board[x][y] - 1][now_dir - 1][me]
                            temp[nx][ny] = board[x][y]
                            break

    board = temp
    time += 1
    check = True
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break

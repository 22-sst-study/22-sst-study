import sys
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

answer = 0
R, C, M = map(int, input().split())
sharkMap = [[0]*C for _ in range(R)]

def changeDirec(d):
    if d ==0 : return 1
    elif d == 1 : return 0
    elif d == 2 : return 3
    elif d == 3 : return 2

def move(x, y, s, d, z): # x, y, 속력, 방향, 크기
    ns, nd = s, d
    if nd == 0 or nd == 1: ns %= (R-1) *2
    else: ns %= (C-1) *2
    
    while ns>0:
        ns -= 1
        direction = directions[nd]
        nx, ny = x + direction[0], y + direction[1]
        if 0<=nx<R and 0<=ny<C: 
            x, y = nx, ny
        else : 
            nd = changeDirec(nd)
            x -= direction[0]
            y -= direction[1]
    return [x, y, s, nd, z]

for _ in range(M):
    x, y, s, d, z = map(int, input().split())
    sharkMap[x-1][y-1] = [s, d-1, z] # 속력, 방향, 크기

for king in range(C):
    ''' 1. 상어 낚시 '''
    for i in range(R):
        if sharkMap[i][king] != 0:
            answer += sharkMap[i][king][2]
            sharkMap[i][king] = 0
            break

    '''2. 상어 이동'''
    tmp = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if sharkMap[x][y] != 0:
                nx, ny, s, nd, z = move(x, y, *sharkMap[x][y])
                if tmp[nx][ny] != 0 :
                    if tmp[nx][ny][2] < z:
                        tmp[nx][ny] = [s, nd, z]
                else:
                    tmp[nx][ny] = [s, nd, z]
    sharkMap = tmp
    
print(answer)
                        
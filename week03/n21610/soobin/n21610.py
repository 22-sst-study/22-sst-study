import sys
input = sys.stdin.readline

direction = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

def findclouds(lastClouds):
    clouds = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not lastClouds[i][j]:
                clouds.append((i, j))
    return clouds

def moveIndex(clouds, directIdx, num):
    temp = []
    def indexOver(x):
        if x < 0:
            if (-1 * x) % N == 0:
                x = 0
            else:
                x = N - ((-1 * x) % N)
        return x % N    
    for i, j in clouds:
        ni = indexOver(i + direction[directIdx][0] * num)
        nj = indexOver(j + direction[directIdx][1] * num)
        temp.append((ni, nj))
    return temp    

def copyWater(i, j):
    tmp = 0
    for k in range(4):
        ni = i + diag[k][0]
        nj = j + diag[k][1]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
            tmp += 1
    arr[i][j] += tmp

def solution():
    clouds =  [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
    for direct, num in move:
        ## lastClouds를 (x, y) 의 list로 하면 
        ## findclouds 할 경우에 O(n)만큼의 시간이 더 필요함
        lastClouds = [[False] * N for _ in range(N)] 
        clouds = moveIndex(clouds, direct, num)
        for i, j in clouds:
            lastClouds[i][j] = True
            arr[i][j] += 1
        for i, j in clouds:
            copyWater(i, j)
        clouds = findclouds(lastClouds)
        for i, j in clouds:
            arr[i][j] -= 2

    answer = 0
    for a in arr:
        answer += sum(a)
    print(answer)

solution()
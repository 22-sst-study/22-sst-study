'''
PyPy3 : 264ms
python : 392ms
'''
'''
손님선택하는 과정에서 BFS각각 다 돌리지X
배열에 거리 다 저장해서 넘기는 BFS함수 
'''

import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M, fuel = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(lambda x : int(x)-1, input().split()))
clients = [list(map(lambda x : int(x)-1, input().split())) for _ in range(M)]
def BFS(x1, y1, x2, y2): ## 이동거리반환
    queue = deque([(x1, y1)])
    visited = [[False]*N for _ in range(N)]
    visited[x1][y1] = True
    table = [[INF]*N for _ in range(N)]
    table[x1][y1] = 0
    while queue:
        if table[x2][y2] != INF: break
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False:
                visited[nx][ny] = True
                if Map[nx][ny] != 1:
                    queue.append((nx, ny))
                    table[nx][ny] = table[x][y] + 1
    return table[x2][y2]  

def BFSAll(x, y):
    queue = deque([(x, y)])
    table = [[INF]*N for _ in range(N)]
    table[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and table[nx][ny]==INF:
                if Map[nx][ny] != 1:
                    queue.append((nx, ny))
                    table[nx][ny] = table[x][y] + 1
    return table

def findClient(x, y):## 택시 현재 위치 
    table = BFSAll(x, y)
    tmp = []
    for i, client in enumerate(clients):
        cx, cy = client[0], client[1]
        tmp.append([table[cx][cy], cx, cy, i])
    return min(tmp)

while clients:
    client = findClient(taxi[0], taxi[1]) # 손님까지거리, 손님x, 손님y, 손님인덱스
    fuel -= client[0]
    if fuel < 0 :
        print(-1)
        break
    clientInfo = clients.pop(client[3])
    distance = BFS(*clientInfo)
    if fuel < distance:
        print(-1)
        break
    else:
        fuel += distance
    taxi = clientInfo[2:]
if not clients:
    print(fuel)

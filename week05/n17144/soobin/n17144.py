'''
pypy3: 688ms
python3: 시간초과..
'''

from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
clockwise = [0, 1, 2, 3]
notclockwise = [0, 3, 2, 1]
machine = (-1, -1)

def spread(arr):
    tmp = deepcopy(arr)
    for x in range(R):
        for y in range(C):
            if arr[x][y] <= 0: continue
            count = 0
            for n in range(4):
                nx, ny = x + directions[n][0], y + directions[n][1]
                if 0<=nx<R and 0<=ny<C and arr[nx][ny] != -1:
                    tmp[nx][ny] += arr[x][y]//5
                    count += 1
            tmp[x][y] -= arr[x][y]//5*count
    return tmp

def move(arr, x, y, way): # x, y:공기청정기 위치 / way: 시계 or 반시계
    nx, ny = x, y+1
    n_direction = 0
    tmp = 0
    while (nx, ny) != (x, y) and arr[nx][ny] != -1:
        tmp ,arr[nx][ny] = arr[nx][ny], tmp    
        tx, ty = nx + directions[way[n_direction]][0], ny + directions[way[n_direction]][1]
        if 0<=tx<R and 0<=ty<C:
            nx, ny = tx, ty
        else:
            n_direction = (n_direction + 1)%4
            nx, ny = nx + directions[way[n_direction]][0], ny + directions[way[n_direction]][1]

for x in range(R):
    if -1 in arr[x]:
        machine = (x, arr[x].index(-1))
        break 
for _ in range(T):       
    arr = spread(arr)    
    move(arr, machine[0], machine[1], clockwise)    
    move(arr, machine[0]+1, machine[1], notclockwise) 

print(sum([sum(row) for row in arr]) + 2)

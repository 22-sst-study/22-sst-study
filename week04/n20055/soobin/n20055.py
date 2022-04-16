from copy import deepcopy
import sys
input = sys.stdin.readline

answer = 0
upIdx = 0 # 올리는 위치의 인덱스
N, K = map(int, input().split())
belts = list(map(int, input().split())) ## 길이 2N
robots = []
count = 0

while True:
    answer += 1
    ## 1. 컨베이어이동
    upIdx = (2*N + upIdx-1)%(2*N)
    downIdx = (upIdx + N-1)%(2*N)
    if downIdx in robots: 
        robots.remove(downIdx)

    ## 2. 로봇 회전방향으로 한칸 이동
    tmp = 0
    for i, robot in enumerate(deepcopy(robots)): 
        nextIdx = (robot+1)%(2*N)
        if (nextIdx not in robots) and (belts[nextIdx] >=1):
            robots[i-tmp] = nextIdx
            belts[nextIdx] -= 1
            if belts[nextIdx] == 0:
                count += 1
            if downIdx in robots:
                robots.remove(downIdx)
                tmp += 1

    ## 3. 올리는 위치 칸의 내구도가 0이 아니면 로봇 올림
    if (belts[upIdx] != 0) and (upIdx not in robots): 
        robots.append(upIdx)
        belts[upIdx] -= 1
        if belts[upIdx] == 0: 
            count += 1

    if count >= K:
        break
    
print(answer)

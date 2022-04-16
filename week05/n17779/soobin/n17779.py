'''
pypy3: 416ms
python3: 1108ms
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
total = sum([sum(a) for a in arr])

def solve(x, y, d1, d2):
    people = [0 for _ in range(5)]
    line = set()
    for n in range(d1+1):
        line.add((x+n, y-n))
        line.add((x+d2+n, y+d2-n)) 
    for n in range(d2+1):
        line.add((x+n, y+n))
        line.add((x+d1+n, y-d1+n)) 

    for i in range(1, x+d1): ## 1번 선거구
        for j in range(1, y+1):
            if (i, j) in line: break
            people[0] += arr[i-1][j-1]
    for i in range(1, x+d2+1): ## 2번 선거구
        for j in range(N, y, -1):
            if (i, j) in line: break
            people[1] += arr[i-1][j-1]
    for i in range(x+d1, N+1): ## 3번 선거구
        for j in range(1, y-d1+d2):
            if (i, j) in line: break
            people[2] += arr[i-1][j-1]
    for i in range(x+d2+1, N+1): ## 4번 선거구
        for j in range(N, y-d1+d2-1, -1):
            if (i, j) in line: break
            people[3] += arr[i-1][j-1]
    people[4] = total-sum(people)
    return max(people) - min(people)

for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    answer = min(answer, solve(x, y, d1, d2))
                else: break
print(answer)
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
arr = [[0] * N for _ in range(N)] ## 학생들이 앉는 자리 
students = [list(map(int, input().split())) for _ in range(N**2)]

for student in students:
    tmp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                like, blank = 0, 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] in student[1:]:
                            like += 1
                        if arr[nx][ny] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    ## like, blank는 큰 순서대로, i, j는 작은 순서대로 
    tmp.sort(key= lambda x : (-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = student[0]

answer = 0
students.sort()
for i in range(N):
    for j in range(N):
        tmp = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] in students[arr[i][j]-1]:
                    tmp += 1
        if tmp != 0:
            answer += 10 ** (tmp-1)
print(answer)
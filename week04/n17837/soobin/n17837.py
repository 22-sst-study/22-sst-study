'''
PyPy3 : 216ms
python : 96ms
'''

import sys
input = sys.stdin.readline

direction = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

answer = 0
overFourPiecesFlag = 0
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] #0: 흰색, 1: 빨간색, 2: 파란색
pieces = [list(map(int, input().split())) for _ in range(K)] ## 배열의 현재 위치
for i in range(K):
    pieces[i][0] -= 1
    pieces[i][1] -= 1
pieceList = {} # (x, y) : [3, 1] # 좌표에 따라 말 인덱스리스트 저장
for i, piece in enumerate(pieces):
    x, y, direc = piece
    pieceList[(x, y)] = [i] # 말번호 0부터 시작

def reverseDir(n):
    if n == 1: return 2
    elif n == 2 : return 1
    elif n == 3 : return 4
    else : return 3

def checkColor(x, y):
    if 0<=x<N and 0<=y<N:
        return arr[x][y] ## 색 리턴
    else:
        return 2 ## 벗어날 경우 파란색 벽 

def move():
    global overFourPiecesFlag 
    tmp = pieceList[(nowX, nowY)][:idx]
    if len(tmp) == 0:
        del pieceList[(nowX, nowY)]
    else: 
        pieceList[(nowX, nowY)] = tmp
    for p in piecestoMove:
        pieces[p][0] = nx
        pieces[p][1] = ny
    if (nx, ny) in pieceList:
        pieceList[(nx, ny)] += piecestoMove
        if len(pieceList[(nx,ny)]) >= 4:
            overFourPiecesFlag = 1
    else:
        pieceList[(nx, ny)] = piecestoMove


while True:
    answer += 1
    if answer >= 1000: 
        print(-1)
        break
    for i in range(K): # i가 이번에 이동할 말의 인덱스
        nowX, nowY, direc = pieces[i]
        idx = pieceList[(nowX, nowY)].index(i)
        piecestoMove = pieceList[(nowX, nowY)][idx:] # 그 위에 얹어져있는 말포함 리스트
        nx = nowX + direction[direc][0]
        ny = nowY + direction[direc][1]
        newColor = checkColor(nx, ny)
        if newColor == 0: ## 이동
            move()
        elif newColor == 1: ## 이동, 이동할때 순서 뒤집힘
            piecestoMove.reverse()
            move()
        elif newColor == 2:
            direc = reverseDir(pieces[i][2])
            pieces[i][2] = direc
            nx = nowX + direction[direc][0]
            ny = nowY + direction[direc][1]
            newColor = checkColor(nx, ny)
            if newColor == 0:
                move()
            elif newColor == 1:
                piecestoMove.reverse()
                move()
    if overFourPiecesFlag == 1:
        print(answer)
        break


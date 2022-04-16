'''안돌아감 ㅜ.ㅜ'''
'''

- 상어정보 입력받은 배열 그대로 사용 sharks : [ [x, y, 속력, 방향, 크기],  ..]
- sharksLoc : 키 : (x, y) / 값 : [속력, 방향, 크기, sharks배열에 저장된 인덱스]

1. 상어 낚시 
2. 상어 이동 
 : 이동시킨 후의 상어정보를 그대로 sharks배열에 저장
3. 두마리 이상일 경우 한마리만 남도록 
 : sharksLoc사용해서 x,y좌표에 상어 있는지 체크하고, 있으면 sharks배열에서 pop해주기

이중포문 안 만들려고 딕셔너리 썼는데 
for 문 내에서 pop하면 인덱스 꼬여서 v2보다 고려할 점이 많았음

'''
import sys
input = sys.stdin.readline

answer = 0
directions = [(), (-1, 0), (1, 0), (0, 1), (0, -1)]

R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]

def changeDirec(d):
    if d ==1 : return 2
    elif d == 2 : return 1
    elif d == 3 : return 4
    else : return 3
    
def move(x, y, s, d, z): # x, y, 속력, 방향, 크기
    ns, nd = s, d
    if nd == 1 or nd == 2: ns %= (R-1) *2
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
    
for i, shark in enumerate(sharks):
    sharks[i][0] -= 1
    sharks[i][1] -= 1

for king in range(C):
    ''' 1. 상어 낚시 '''
    sharks.sort()  
    for i, shark in enumerate(sharks):
        if shark[1] == king:
            dShark = sharks.pop(i)
            answer += dShark[4]
            break

    ''' 2. 상어 이동'''
    for i, shark in enumerate(sharks):
        sharks[i] = move(*shark)

    ''' 3. 이동한 후 상어가 겹치면 크기가 큰 애가 살아남도록 '''
    sharkLoc = {}  # [속력, 방향, 크기, sharks배열에 저장된 인덱스]
    idxtoPop = []
    for i, shark in enumerate(sharks):
        if (shark[0], shark[1]) in sharkLoc:
            if sharkLoc[(shark[0], shark[1])][2] > shark[4]:
                idxtoPop.append(i)
            else:
                idxtoPop.append(sharkLoc[(shark[0], shark[1])][3])
                sharkLoc[(shark[0], shark[1])] = [*shark[2:], i]
        else:
            sharkLoc[(shark[0], shark[1])] = [*shark[2:], i]
    for i in reversed(idxtoPop) :
        sharks.pop(i)

print(answer)

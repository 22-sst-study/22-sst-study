'''
PyPy3 : 276ms
python : 156ms
'''

import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
answer = 0
blockstoPut = [list(map(int, input().split())) for _ in range(N)]
greenArr = [[0, 0, 0, 0] for _ in range(6)]
blueArr = [[0, 0, 0, 0] for _ in range(6)]

def fill(t, x, y, arr):
    y_tmp = []
    if t == 2: #1x2
        y_tmp = [y, y+1]
    else: 
        y_tmp = [y]
    index = INF
    for yy in y_tmp:
        tmp_index = -1
        for i, row in enumerate(arr):
            if row[yy] == 0 : 
                tmp_index = i
            else:
                break
        index = min(index, tmp_index)

    arr[index][y] = 1
    if t == 2 : #1x2
        arr[index][y+1] = 1
    elif t == 3: #1x2
        arr[index-1][y] = 1  

def checkSpecialBlocks(arr):
    tmp = 0
    for i in range(2):
        if sum(arr[i]) > 0:
            tmp += 1
    while tmp > 0:
        arr.pop(-1)
        arr.insert(0,[0,0,0,0])
        tmp -= 1      

def checkFullBlocks(arr):
    global answer
    for i, row in enumerate(arr):
        if sum(row) == 4:
            answer += 1
            arr.pop(i)
            arr.insert(0,[0,0,0,0])

for idx, block in enumerate(blockstoPut):
    fill(*block, greenArr)
    if block[0] == 2: block[0] = 3
    elif block[0] == 3 : block[0] = 2
    block[1], block[2] = block[2], block[1]
    fill(*block, blueArr)
    
    checkFullBlocks(greenArr)
    checkFullBlocks(blueArr)

    checkSpecialBlocks(greenArr)
    checkSpecialBlocks(blueArr)

print(answer)
print(sum([sum(a) for a in greenArr]) + sum([sum(a) for a in blueArr]))
# 구슬 탈출 2
https://www.acmicpc.net/problem/13460

## Step
1. 상하좌우 4방향으로 탐색
   1. 이동
      1. 빨강 구슬 이동
      2. 파랑 구슬 이동
      3. 빨강 구슬 이동
      4. (이유는 파랑 구슬 이동 후에 빨강 구슬이 이동 가능해질 수도 있으므로 한 번 더 이동 시켜본다)
   2. 종료 조건
      1. 빨강 구슬만 골 인 -> 성공
      2. 파랑 구슬도 골 인 -> 실패
      3. 이동 횟수가 10회 초과 -> 실패
2. 1 반복

## 풀이
### 기울였을 때 벽까지의 이동
- 한 번 기울였을 때를 한 번의 이동이라고 간주
- 한 번의 이동시 벽, O, 구슬에 닿을 때까지 쭉 간다.
- 한 칸 한 칸 이동시마다 배열 정보를 수정할 필요 없이, 이동 종료시에 마지막 위치만 변경 해주면 된다.

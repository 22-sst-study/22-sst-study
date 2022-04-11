# 연구소 3
https://www.acmicpc.net/problem/17142

## Step
1. 벽을 제외한 나머지 공간의 수 (target)와 바이러스 놓을 수 있는 위치 저장(m_candidates)
2. 바이러스 놓을 수 있는 위치 저장
3. 저장된 위치 중에서 m개를 뽑음
   1. 동시 bfs
   2. cnt 수가 target만큼 되면 정답 후보군에 저장
4. 출력

## 풀이
### bfs 캐싱 필요
- 경우의 수 마다 bfs를 돌려서 너무 오래 걸림

## 결과

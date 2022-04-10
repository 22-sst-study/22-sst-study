# 새로운 게임 2
https://www.acmicpc.net/problem/17837

## Step
1. 말 이동
2. 한 칸에 4개가 모였는지 체크

## 풀이
### 엎혀 있는 말을 모두 이동시키기
- 2차원 배열의 각 위치에 deque를 선언했다.
- 선언한 deque에는 `Mal` 클래스의 객체를 넣었다.
- 말을 이동(`move`)시킨다면 해당 말이 기존에 위치하던 장소의 deque를 탐색한다.
- 타겟 말이 나올 때까지 pop.
- pop한 말들은 별도의 리스트에 저장해두고, 이동할 위치 칸의 색에 따라 저장하는 방법을 달리한다.
- 이동할 위치가 white라면 reverse한 상태로 extend, red라면 그냥 extend한다.
- pop 할 때 이미 순서가 뒤집혔기 때문.

## 결과
![image](https://user-images.githubusercontent.com/41278416/161500717-234656b1-2ddf-4bf5-9580-2f7a27c83534.png)

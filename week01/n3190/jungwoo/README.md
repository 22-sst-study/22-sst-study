# 뱀
https://www.acmicpc.net/problem/3190

## Step
1. 이동
   1. 머리 이동
       1. 이동 위치가 벽 바깥 or 자기 몸 -> 실패 -> 종료
       2. 이동한 위치가 사과 -> 1-2 생략
   2. 꼬리 이동
2. 방향 전환
3. 1~2 반복

## 풀이
### 머리 정보와 꼬리 정보 저장 관련
- `snake` 변수에 머리를 add 하고 꼬리를 pop 했다.
- 사과를 만났을 때는 pop을 생략하면 되니 간편.
- add 할 때는 위치 정보를 넣음.

### 방향 정보와 다음에 이동할 위치를 얻기
- `Head` 클래스를 만들어 사용했다.
- r, c, idx 필드를 가지며 각각 행, 열, 방향 인덱스를 표시.
- get_next_pos 함수를 통해 head 객체가 현재 갖고 있는 방향에서 한 칸 이동한 위치를 구할 수 있다.
- 위에서 구한 위치 정보가 움직일 수 있는지 판단하고 set_pos를 통해 객체의 r, c 필드를 업데이트.
- 방향 인덱스는 이동 후에 객체 바깥에서 업데이트시켜준다.
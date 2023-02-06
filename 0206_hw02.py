# 첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
T = int(input())
for tc in range(1, T+1):
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
    N = int(input()) # N개의 색박스가 만들어짐
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
# color = 1 (빨강), color = 2 (파랑)
    box1 = [[0 for _ in range(10)] for _ in range(10)] # 빨강을 칠할 리스트
    box2 = [[0 for _ in range(10)] for _ in range(10)] # 파랑을 칠할 리스트
    count = 0 # 빨강과 파랑이 겹치는 칸
    for _ in range(N): # N개의 박스 순회
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1: # 빨강일 때
            for i in range(r1, r2+1): # 열
                for j in range(c1, c2+1): # 행
                    box1[i][j] += color # 빨강을 칠할 리스트에 해당 좌표들의 값(1)을 저장
        else:
            for i in range(r1, r2 + 1): # 열
                for j in range(c1, c2 + 1): # 행
                    box2[i][j] += color # 파랑을 칠할 리스트에 해당 좌표들의 값(2)을 저장

    for i in range(10): # 10칸을 순회
        for j in range(10):
            if box1[i][j] and box2[i][j]:
                # '=='연산자 안 쓰는 이유 -> box1(1)과 box2(2)의 값이 달라 비교를 할 수가 없음!
                count += 1
    print(f'#{tc} {count}')
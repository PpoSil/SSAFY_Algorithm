# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
T = int(input())
for tc in range(1, T+1):
    # 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
    N, M = map(int, input().split())
    # 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
    arr = list(map(int, input().split()))

    # 가장 큰 합
    mxSum = 0

    # 가장 작은 합 # 리스트의 값을 다 더한 값이 가장 작은 수임!!!!
    mnSum = 0
    for my_sum in arr: # 리스트 요소 순환
        mnSum += my_sum

    # arr 리스트에서 인덱스 순회 i: 0 # 첫번째 인덱스!!!!! -> N-M+1(이게 제일 마지막거)
    for i in range(N-M+1): # N-M+1 -> 범위를 벗어나지 않는 마지막 i값
        # 합 변수
        total = 0
        for j in range(i, M + i): # M+i -> i와 함께 M만큼 움직임
            total += arr[j]
            # i부터 M+i 범위(== arr[j]의 합이 가장 클 경우
        if total > mxSum:
            mxSum = total # mxSum에 저장
            # i부터 M+i 범위(== arr[j])의 합이 가장 작은 경우
        if total < mnSum:
            mnSum = total # mnSum에 저장
    print(f'#{tc} {mxSum - mnSum}') # 가장 큰 합과 가장 작은 합의 차
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
T = int(input())
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
for tc in range(1, T+1):
    # 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
    N = int(input())
    arr = list(map(int, input().split()))

    my_max = arr[0] # 최댓값이 arr 리스트의 1번째 값부터

    my_min = arr[0] # 최솟값이 arr 리스트의 1번째 값부터

    for i in range(1, N): # 최댓값, 최솟값 2번째거부터 비교해야되니까 인덱스 1번부터!
        if arr[i] > my_max: # my_max값이 arr[i]보다 작다면
            my_max = arr[i] # arr[i]값이 가장 큰거니까 my_max에 저장
        if my_min > arr[i]: # my_min값이 arr[i]보다 크다면
            my_min = arr[i] # arr[i]값이 가장 작은거니까 my_min에 저장
    print(f'#{tc} {my_max-my_min}')
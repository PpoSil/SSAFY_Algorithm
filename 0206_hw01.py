# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
T = int(input())
for tc in range(1, T+1):
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )
    N, K = map(int, input().split()) # 비교할 값: 집합 A의 부분 집합 중 N개의 원소, 원소의 합 K
    A = list(range(1, 13)) # A가 1~12까지
    count = 0
    for i in range(1<<len(A)): # 부분 집합의 개수
        total = 0 # 부분 집합의 합
        lst = [] # 부분 집합
        for j in range(len(A)): # 이진수의 길이만큼!!!!!
            if i & (1<<j): # i의 j번 비트가 1인 경우
                lst.append(A[j])
                total += A[j]
        if N == len(lst) and K == total:
            count += 1
    print(f'#{tc} {count}')
import sys
sys.stdin = open('input.txt', 'r')

# 총 18개의 테스트케이스가 주어진다.
for tc in range(1, 11):

# 각 테스트케이스의 첫 번째 끝에는 건물의 개수 N이 주어진다. (4 <= N <=1000)
    n = int(input())
# 그 다음 줄에는 N개의 건물의 높이가 주어진다.(0<= 각 건무르이 높이 <= 255)
    buildings = list(map(int, input().split()))
    result = 0 # 나중에 사용할 결과값
# 빌딩을 순회한다. i : [2, n-2)
    for i in range(2, n -2):
        mx = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if buildings[i] > mx:
            result += buildings[i] - mx
    print(f'#{tc} {result}')
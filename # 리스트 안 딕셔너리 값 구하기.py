#리스트 안에 딕셔너리 있는 값 가져오기 문제 (age의 합을 구하세요)
infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

#인덱스 함수로
total1 = 0 # 나이를 더해줄 함수 선언

for i in range(len(infos)): # infos를 순회
    total1+= list(infos[i].values())[1] 
    # infos의 (i번째 딕셔너리에서 values들)을 가져오는데 그 values들 중 age는 1번 인덱스에 있으니 가장 바깥쪽
    # + .keys / .values / .items는 list형식으로 변환 x
    # so 더해주려면 list로 변환 필요 ex) list(a.keys())
print(total1)

#or

# get함수로
total2 = 0 # 나이를 더해줄 함수 선언

for i in range(len(infos)): # infos를 순회
    total2 += infos[i].get('age') 
print(total2)
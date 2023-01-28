# list(리스트) 메소드
# 변경o 순서o 순회o

# 추가: .append() 리스트에 추가
# 정해진 위치에 추가: .insert(i(위치),x(값))

# .append(x) vs .extend(iterable)
# append는 그대로 더함 []형식이면 [] 그대로!
# extend는 리스트든 문자열이든 다 풀어서 더함

# 제거
# .remove(x): 리스트의 첫번째 x값을 삭제- 여러개 삭제하려면 여러번! 값이 없다면 error

# 제거 & 반환: .pop([i])
# 제거할 땐 a.pop([i])를 한 후 print(a) 해보면 [i]의 값이 a에서 삭제되어있음
# print(a.pop[i])를 하면 a리스트의 [i]만 반환 가능

# 모두 삭제: .clear()

# 위치 반환:  .index(x) 값이 없으면 error

# 원하는 값의 개수 반환: .count(x)

# 정렬: a.sort() vs b.sorted()
# a.sort()는 a 자체를 정렬시켜줌. 새로운 리스트 생성 x / 역순은 .sort(reverse=True)
# so print(a.sort())를 하면 None을 반환함
# b.sorted()는 b의 값들을 정렬시켜 새로운 리스트를 생성함.
# so b.sotred()를 print하면 b와 다른 리스트가 나옴.
# +
# ex1) .sort() # [1, 2, 3, 5, 7] / None
# some_list = [5, 7, 2, 3, 1]
# print(sorted(some_list))
# print(some_list.sort())
# +
# ex2) .sorted() # [1, 2, 3, 5, 7]
# some_list = [5, 7, 2, 3, 1]
# some_list.sort()
# print(some_list)

# 역순: .reverse()
# 원본과 다른 역순 리스트 생성
# if print(a.reverse()) # None != print(a)
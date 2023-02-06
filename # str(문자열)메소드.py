# string(문자열) 메소드
# 변경 x / 순서 o / 순회 o

# .find(x) vs .index(x)
# .find(x): x의 첫 번째 위치 반환. 리스트 내에 x가 없으면 -1
# .index(x): x의 첫 번째 위치를 반환. 리스트 내에 x가 없으면 error

# .startswith(x) 
# 접두/접미사/ 문자열이 x로 시작하면 True, 아니면 False

# .endswith(x)
# 접두/접미사/ 문자열이 x로 끝나면 True, 아니면 False

# 문자열 검증 메서드
# .isalpha() : 문자열이 (숫자가 아닌)글자로?
# .isspace() : 문자열이 공백?
# .isupper() : 문자열이 대문자?
# .istitle() : 문자열이 타이틀 형식?
# .islower() : 문자열이 소문자?

# 숫자 판별 메서드
# .isdecimal(): 문자열이 0~9까지의 수로?
# .isdigit(): 문자열이 숫자?
# .isnumeric(): 문자열을 수로 볼 수 있는가?

# 문자열 변경
# 변경: .replace(old, new, [,count(몇 개를?)] old를 new로 변경
# 제거: .strip([chars]) 지정 문자열 제거. 인자가 없으면 공백 제거(양쪽 다 가능)
# + .lstrip([chars]) 왼쪽에서부터 / .rstrip([chars]) 오른쪽에서부터
# 특정 단위로 나누기(리스트로 변환): .split([chars]) 
# 'separator(구분자)'.join(iterable(순회가능한 문자열)): 구분자로 나누어줌
# 대문자로: .capitalize()
# '나 공백 이후 대문자로 만들어 반환: .title()
# 모두 대문자로: .upper()
# 모두 소문자로: .lower()
# 대<->소문자로: .swapcase()

# 해당 문자가 포함되어있는지 여부 확인
# '해당 문자' in '문자열'

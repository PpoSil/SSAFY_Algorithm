# <객체 지향 프로그래밍>
# 생성자 메소드 중
# 속성 정의 유무의 차이

# 1. 속성 정의가 없을 경우
# ex1)
class Person:
    def talk(self): # 1) if (self, fd) 이런식으로 정의가 된다면
        print('안녕') # 2) 1.에는 self.fd = fd 이런 속성이 없음

    def eat(self, food): 
        # if 위의 food에 아무 값이 저장이 안 되어있을 때 eat(빈 값)메소드를 활용하여 출력하면 에러뜸
        # if 위의 food에 예를 들어 food = '간식내나'를 eat(빈 값)으로 출력하면 # "냠냠 간식내나"가 뜸
        print(f'냠냠 {food}')

p1 = Person() # 3) so p1에 Person 클래스를 활용하여 인스턴스 생성
p1.eat('젤리') # 4) talk() 메서드를 호출하면 # '냠냠 젤리'가 출력
p1.eat('깎아')
p1.eat()

# 2. 속성 정의가 있을 경우 (__init__함수를 사용하지 않을 경우)
# ex2)
class Person: 
    # def talk(self, talk):
    #     self.talk = talk

    def eat(self, food): # person을 받을 self와 음식을 받을 food 변수
        self.food = food # 변수 self.변수food = 변수food (속성 설정)
        print(f'냠냠 맛있는 {food}') 
        
    # def __init__(self, eat):
    #     self.eat = eat
    #     print(f'냠냠 맛있는 {eat}')

p1 = Person() # p1 인스턴스 생성
p1.eat('jelly') # eat()함수를 활용하여 호출
p1.eat('banana')
p1.eat('apple')
# p1 한 명이 젤리 바나나 사과 이런 식으로 한 명이 여러 음식을 먹을 수 있음!!!
# 여러개의 값을 할당 가능할지도..?


# 3. 속성 정의가 있을 경우2 (__init__함수를 사용하는 경우)
# ex3)
class Person:
    # def talk(self, talk):
    #     self.talk = talk
        
    def __init__(self, eat):
        self.eat = eat
        print(f'냠냠 맛있는 {eat}')

p1 = Person('jelly') # 젤리만 먹고 살아야 함. # 굳이 p1.eat('변수') 이런거 더 안 적어도 됨!!!! 
p1 = Person('apple') # p1에 들어있는 것처럼 보이지만 사실은 주인이 없음. 이미 p1에는 젤리가 할당되어있음!
p1 = Person() # error
# 위의 p1과 아래의 p1이 같은 변수명이지만 밑의 p1의 사과는 주인을 잃어버림.
# 하나의 값만 할당 가능할 때 쓰는 쪽..?

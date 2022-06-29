# Chapter02-02
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Car():
    """
    Car Class
    Author : Kim
    Date : 2019.11.08
    """
    # => 이걸 다는 이유는?
    # Doctring => Car.__doc__
    
    # 클래스 변수 - 모든 인스턴스가 공유
    # 인스턴스에 속하는 스코프가 아니기 때문에 __dict__에서는 안보인다. dir에서는 보임
    # 보통 언더바를 안붙인다.
    car_count = 0

    # self : 인스턴스 변수 
    def __init__(self, company, details):
        self._company = company
        # 클래스 변수와 같은 이름을 사용하게 되면 이것이 더 먼저 조회된다.
        # self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1

# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
# 인스턴스마다 다르다.
# self가 있어야 같은 클래스를 사용하는 인스턴스들을 구별할 수 있게 된다.
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # 값의 비교, False
print(car1 is car2) # 인스턴스 자체 비교, id가 다르니 False

# dir & __dict__ 확인
# dir: 해당 인스턴스의 모든 정보를 표현
# 모든 클래스는 object를 상속받기 때문에 dir 하면 object의 모든 정보도 추출된다.
print(dir(car1))
print(dir(car2))

print()
print()

# dir이 너무 많은 정보를 담아서 싫다!
# 필요한 것만 보고 싶다면 __dict__ 사용
# 해당 인스턴스의 네임스페이스에만 속하는 정보들을 딕셔너리로 보여준다. 
print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()

# 에러
Car.detail_info() #=> 이렇게 하면 self가 없다고 에러가 발생한다. 
Car.detail_info(car1) # => 사실 car1.detail_info()를 실행하면 첫번째 인자로 car1 자체가 전달되고 있던 것이다.
Car.detail_info(car2)

# 비교
# __clsas__를 사용하면 인스턴스의 템플렛이 되는 클래스 정보를 얻을 수 있다. 
print(car1.__class__, car2.__class__) # class Car
print(id(car1.__class__) == id(car3.__class__)) # 클래스 자체의 id는 같다. 

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)
print(car1._company, car2._company)
print(car2._company, car3._company)

print()
print()

# 클래스 변수

# 접근
print(car1.car_count)
print(car2.car_count)
print(Car.car_count)

print()
print()

# 공유 확인
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
del car2

print(car1.car_count)
print(Car.car_count)
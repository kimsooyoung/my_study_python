# Chapter02-01
# 파이썬 중급
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 비공식적, print로 출력할 떄 등장하는 것임
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    # 엄격, 객체를 표현할 때는 repr을 사용한다.
    # 만약, str이 없으면 print()시 이것이 출력된다.
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)


car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 클래스 안의 모든 클래스 속성들을 딕셔너리 형태로 볼 수 있다.
# 메타 프로그래밍 시 사용하는 dir도 있음
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

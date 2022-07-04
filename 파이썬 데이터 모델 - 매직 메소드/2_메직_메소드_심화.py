# Chapter03-02
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 클래스 예제2
# 벡터를 계산해주는 패키지를 만들어달라는 문의를 받았다고 하자.
# ex) (1,2) + (3,4) => (4,6)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10
class Vector(object):
    # (self, x, y)를 좀 더 세련되게 하자.
    def __init__(self, *args):
        '''
        Create a vector, example : v = Vector(5,10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Returns the vector infomations'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    # 벡터끼리 더하기
    def __add__(self, other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)
    
    # 벡터끼리 곱하기
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    # (0,0)인지 확인하는 메소드
    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23, 35)
# 0,0 생성해보기
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)

# (0,0) 인지 확인하기
print(bool(v1), bool(v2))
print(bool(v3))

print()
print()

# 참고 : 파이썬 바이트 코드 실행
import dis
dis.dis(v2.__add__)
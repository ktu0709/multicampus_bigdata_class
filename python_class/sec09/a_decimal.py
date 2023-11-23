import decimal
from decimal import * #-> 부동 소숫점 정밀도 계산 모듈
# 부동 소수점 정밀도 -> 부동소숫점 숫자는 이진수로 표시 / 특정 소수점을 2진수로 표시가 안되는 경우가 발생한다
#(90.7+30.2) + 0.0002  , print(120.9)  -> 부동 소숫점 반올림 오류 120.90020000000001

def case01():
    res = Decimal("90.7")+Decimal("30.2") + Decimal("0.0002")
    print(res , type(res))
    print(1/3)
    print(decimal.getcontext())  # 부동소숫점 환경설정값을 출력
    decimal.getcontext().prec=3
    a,b = Decimal("1")  , Decimal("3")
    print(a/b)

    a, b = Decimal("5"), Decimal("7")
    print(a / b)

    c=Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-425000000, Emax=425000000, capitals=1, clamp=0, flags=[], \
            traps=[InvalidOperation, DivisionByZero, Overflow])

    decimal.setcontext(c) # 부동소숫점 환경설정 변경
    print(decimal.getcontext())
    print(decimal.ExtendedContext)
    decimal.setcontext(decimal.ExtendedContext)
    print(decimal.getcontext())
if __name__ == '__main__':
    case01()



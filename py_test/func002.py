# 숫자를 제곱하는 함수 :
# 타입힌트는 예외(에러,오류)를 발생시키지않고, 문법적인 효과가 없다 
def asdf(num:int)->int:      
    # int가 아니면 실패하게 만들자 -> int 어떻게? 실패는 뭐지?
    if isinstance(num, int)==False:
        return 0
    return num*num

# 파이썬,js는 동적타입 -> 정적타입으로 가자
# 자바는 정적타입 -> 동적타입으로 가자
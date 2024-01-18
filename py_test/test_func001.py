# from func001 import sample1
# from func001 import is_major
# from func001 import passport
from py_test.func001 import ten_over

# 테스트하는 함수를 작성: test_XXXXX.py
# 테스트하는 함수는 pytest로 실행이 가능
# 파이테스트 다운 방법 터미널 명령어 : pip install pytest
# 테스트는 assert를 사용해서 확인
# return이 없으면 테스트가 불가능하다
# unit test(단위 테스트)
# def test_sample1():
#      assert sample1()==10

# def test_round():
#     assert round(2.5)==3

# def test_is_major():
#     assert is_major(20) is True
#     assert is_major(18) is True
#     assert is_major(15) is False

# 나이를 입력받아 입장료를 리턴하는 함수
# 25~64세면 3000원 기타는 무료

# def test_passport():
#     assert passport(70)

# 입장료는 3000원이다. 10명이면 1인당 2400원이다.
# 인원수를 입력받아 요금을 출력
def test_ten_over():
    assert ten_over(10)==10*2400
    assert ten_over(9)==9*3000
    assert ten_over(11)==11*2400


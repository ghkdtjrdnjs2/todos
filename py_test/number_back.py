# 데이터 자체는 원래 백이 아니라 datebase에서 관리
# front는 사용자와 입출력하는 view를 담당(터미널,웹,안드로이드,아이폰)
# 백은 처리를 담당하고 view와 상관없이 재사용하고 싶다
# 백을 재사용하려면 백에는 절대 view 관련 코드가 없어야 한다

# numbers_back.py
# test_back.py
# number_front.py

numbers = []

def save(num:int)->bool:
    if isinstance(num, int)==False:
        return False
    numbers.append(num)
    return True
# 딱히 출력할게 없으면 bool로 해라

def find_all()->list:
    return numbers

def delete(num:int)->bool:
     if isinstance(num, int)==False:
        return False
     for item in numbers:          # 넘버스 안에있는 아이템을 가져와라
         if item==num:              # 아이템이 넘버와 같다면   
             numbers.remove(item)   # 넘버스안에 아이템을 지워라
             return True            # True로 표시하고 함수를 종료해라
         return False               # 넘버스 안에 넘버가 없다면 False로 표시하고 함수를 종료해라
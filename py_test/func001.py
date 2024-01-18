def sample1():
    return 10

# 나이를 입력받아 성년/미성년을 판단하는 함수
# def is_major(nai:int)->bool:
#     return nai>=18

def passport(nai:int)->int:
    if nai>=24:
        return 3000
    elif nai>=64:
        return 3000
    else:
        return 0
    
def ten_over(people:int)->int:
    if people>=10:
        print(people)
        return 2400*people   
    elif people<10:
        print(people)
        return 3000*people
  
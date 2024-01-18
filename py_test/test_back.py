import number_back as n
# 임폴트 넘버백을 가져와서 n 으로 이름을 붙인다

# 정수만 저장한다
# def test_save():
#    assert n.save(10) is True
#    assert n.save('10') is False
#    assert n.save(3.14) is False

# find_all 넘버스 안에 있는 리스트를 전부 다 읽어오는것
# def test_find_all():
#    assert len(n.find_all())==0
#    n.save(100)
#    assert len(n.find_all())==1

#삭제
def test_delete():
    n.save(10)
    n.save(20)
    n.save(30)
    assert n.delete(20)==True
    assert len(n.find_all())==2
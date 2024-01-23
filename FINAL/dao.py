import datetime

board = []
board.append(dict(bno=1,title="aa",content="aaa",nickname="spring",readcnt=0))
board.append(dict(bno=2,title="bb",content="bbb",nickname="spring",readcnt=0))
board.append(dict(bno=3,title="cc",content="ccc",nickname="spring",readcnt=0))
b = dict(bno=1, title='title', writeday='writeday', nickname='nickname', content='content' )
bno = 4



def findall()->list:
    return board

# def findone():
#     for b in board:
#         return

def save(title:str, nickname:str, content:str)->bool:
    global bno
    writeday = datetime.datetime.now().date()
    b = dict(bno=bno, title=title, nickname=nickname, content=content, writeday=writeday, readcnt=0)
    board.append(b)
    bno=bno+1
    return True



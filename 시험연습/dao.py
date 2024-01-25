import datetime

board_list=[]
bno = 1

def save(title=str,content=str, nickname=str)->bool:
    global bno
    board = dict(bno=bno, title=title, nickname=nickname, content=content, writeday=writeday, readcnt=0)
    board_list.append(board)
    writeday= datetime.datetime.now().date()
    bno+=1
    return True

def findall():
    return board_list

def findone(bno:int)->dict:
    for board in board_list:
        if board['bno']==bno:
            return board
    return None

    
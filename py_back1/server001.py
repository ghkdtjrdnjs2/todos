from flask import Flask, request
# request 사용자 정보를 담고있는 
# class -> 사용자 정의 자료형을 만드는 방법. 파이썬은 모든 타입이 클래스
# class의 변수는 객체다 (객체) = class
x = int()

# __name__은 현재 파일의 이름 -> Flask 웹서버 객체를 생성
# 서버는 사용자 요청을 기다리다가 요청이 들어오면 처리해주는 프로그램이다
# Flask 웹서버는 5000번 포트로 사용자 요청을 대기한다
app = Flask(__name__)

# annotation - 낙인 찍는 것
@app.route("/hello")
def hello():
    return "hello flask"

@app.route("/hello2")
def insa():
    return "안녕하세요"
 
def add():
    # request로 전달받은 값은 무조건 글자 (인터넷의 규칙) 인터넷을 왔다갔다하는건 다 문자다
    val = request.args['val']
    return val

@app.route('/hello4')
def 제곱():
    val = int(request.args['val'])
    result = val*val
    return f'제곱 결과는 {result}입니다'

@app.route('/hello5')
def 적정체중():
    ki = int(request.args['ki'])
    weight = ki - 105
    return f'적정체중은{weight}입니다'
app.run()
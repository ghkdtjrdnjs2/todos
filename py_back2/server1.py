from flask import Flask, request , render_template

# app = Flask(__name__) 이렇게 써야함 그냥 외우기
app = Flask(__name__)

# 배포서술자(deployment descriptor : 함수와 주소의 쌍)
@app.route("/hello")
def aaa():
    # 플라스크 함수의 리턴은 반드시 문자열이여야한다 그냥 외우기
    return render_template("index.html")

# 어떤 작업을 하려면 화면을 보여준다(get방식) + 결과를 처리하고 출력한다(post) 이 두개가 있어야한다
# get은 보여주고 post는 처리하고 출력한다
# 이름을 입력받아 출력
@app.route("/name", methods=['get'])
# get방식 요청 데이터 : request.args
def name_input():
    return render_template('name.html')


@app.route("/name", methods=['post'])
def name_print():
    # post방식 요청 데티어 : request.form
    name = request.form['irum']
    nai = request.form['nai']
    return render_template("name_result.html", name=name, nai=nai)


# 현재 서버의 모든 url을 출력해라
# print(app.url_map)



# 실행되는 url : 127.0.0.1:5000
# debug란 개발 모드
# app.run 실행시키는것 debug=True는 F5말고 터미널 명령창에 python XXXXXX.py 입력
app.run(debug=True) 




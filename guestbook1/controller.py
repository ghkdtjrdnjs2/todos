# import flask as f
from flask import Flask,request,render_template,redirect
import model as m

# 플라스크 앱(백엔드 서버)을 생성. 인자는 현재 파일의 이름
app = Flask(__name__)

# 방명록을 출력 : 127.0.0.1:5000
# 함수란 요청하는것
@app.route("/")
def list():
    guestbook = m.findall()
    # list.html에 list란 이름으로 guestbook을 넘겨준다
    return render_template("list.html", list=guestbook)

@app.route("/write", methods=['post'])
def write():
    content = request.form.get('content', type=str)
    m.save(content=content)
    return redirect("/")

@app.route("/delete", methods=['post'])
def delete():
  gno = request.form.get('gno', type=int)
  m.delete(gno)
  return redirect("/")

# # 서버를 개발자 모드(변경하면 자동 재실행)로 실행
app.run(debug=True)
# render_template : get. html을 출력
# redirect : post. 처리하고 새로운 주소로 이동

from flask import Flask, request, render_template, redirect
app = Flask(__name__)

todos=[]
tno=1

# 내용을 출력하는 페이지
@app.route('/list')
def list():
    return render_template("list.html", todos=todos)


@app.route('/write')
def write_input():
    return render_template("write.html")


@app.route('/write', methods=['post'])
def do_write():
    # 값을 변경하려면 global 사용
    # 전역 변수 : 모든 함수가 접근가능한 공유 데이터
    global tno
    title = request.form.get("title", type=str)
    todo = {"tno":tno, "title":title, "finish":False}
    todos.append(todo)
    tno=tno+1
    return redirect("/list")

@app.route("/delete", methods=['post'])
def delete():
    id = request.form.get('tno', type=int)
    for todo in todos:
        if todo['ton']==id:
            todos.remove(todo)
            break
    return redirect("/list")
    
app.run()
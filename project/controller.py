from flask import Flask,request,render_template,redirect
import dao

app = Flask(__name__)

@app.route("/")
def 목록():
    board_list = dao.findall()
    return render_template("/list.html", list=board_list)


@app.route("/write")
def 쓰기화면():
    return render_template("/write.html")


@app.route("/read")
def 읽기():
    bno = request.args.get('bno', type=int)
    board=dao.findone(bno)
    return render_template("/read.html", board=board)


@app.route("/write", methods=['post'])
def 쓰기처리():
    title = request.form.get('title', type=str)
    content = request.form.get('content', type=str)
    nickname = request.form.get('nickname', type=str)
    dao.save(title,content,nickname)
    return redirect("/")


@app.route("/update", methods=['post'])
def 변경():
    bno = request.form.get('bno', type=int)
    title = request.form.get('title', type=str)
    content = request.form.get('content', type=str)
    dao.update(bno,title,content)
    return redirect("/")


@app.route("/delete", methods=['post'])
def 삭제():
    bno = request.form.get('bno', type=int)
    dao.delete(bno)
    return redirect("/")

app.run(debug=True)
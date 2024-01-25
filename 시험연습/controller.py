from flask import Flask,redirect,request,render_template
import dao

app=Flask(__name__)
@app.route("/")
def 목록():
    board_list = dao.findall()
    return render_template("/list.html", list=board_list)

@app.route("/read")
def 읽기():
    bno = request.args.get(bno, type=int)
    board=dao.findone(bno)
    return render_template("/read.html", board=board)

@app.route("/write")
def 쓰기화면():
    return render_template("/write.html")

@app.route("/write", methods=['post'])
def 쓰기():
    title=request.form.get('title', type=str)
    content=request.form.get('content', type=str)
    nickname=request.form.get('nickname',type=str)
    dao.save(title, content, nickname)
    return redirect("/")


app.run()
from flask import Flask, request, render_template, redirect
import dao
app = Flask(__name__)

@app.route("/", methods=['get'])
def title():
    result = dao.findall()
    return render_template("/list.html", list=result)

# /read?bno=1 또는 /read?bno=2
@app.route("/read", methods=['get'])
def read():
    bno = request.args.get("bno", type=int)
    board = dao.findone(bno)
    return render_template("/read.html", board=board)

@app.route("/write", methods=['get'])
def write_view():
    return render_template("/write.html")

@app.route("/write", methods=['post'])
def write():
    title = request.form.get('title', type=str)
    nickname = request.form.get('nickname', type=str)
    content = request.form.get('content',type=str)
    dao.save(title=title, nickname=nickname, content=content)
    return redirect("/")


app.run(debug=True)
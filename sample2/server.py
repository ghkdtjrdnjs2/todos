from flask import Flask,request,render_template,redirect

app = Flask(__name__)

todos = []
tno = 1

@app.route("/list")
def list():
    return render_template("list.html", todos=todos)   

@app.route("/write")
def write_input():
    return render_template("write.html")

@app.route("/write", methods=['post'] )
def do_write():
    title = request.form.get("title", type=str)
    todo = {"tno":tno, "title":title, "finish":False}
    todos.append(todo)
    tno=tno+1
    return redirect("/list")

app.run()
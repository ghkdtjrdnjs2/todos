from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/aaaa", methods=['get'])
def name_input():
    return render_template("name2.html")

@app.route("/aaaa", methods=['post'])
def cname_input():
    name2=request.form['irum']
    cname=request.form['dosi']
    return render_template("cname.html", name2=name2 ,cname=cname)





app.run(debug=True)
from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/hi")
def course():
    return"<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html",datetime = str(now))

@app.route("/welcome", methods = ["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name = user)

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/account",methods = ["GET","POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是："+ user + "<br>密碼：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/")
def index():
    homepage = "<h1>李心如 Python 網頁</h1>"
    homepage += "<a href=/hi>Hi~</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=xinru>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>李心如簡介網頁</a><br>"
    homepage += "<a href=/account>表單</a><br>"
    return homepage

# if __name__ == "__main__":
#     app.run()
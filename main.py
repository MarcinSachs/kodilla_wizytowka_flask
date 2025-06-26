from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)


@app.route('/mypage/me')
def me():
    return render_template("me.html")


@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        message = request.form.get("message")
        print(f"Przesłana wiadomość: {message}")
        return redirect("/mypage/me")

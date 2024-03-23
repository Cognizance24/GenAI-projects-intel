
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")
@app.route("/chat.html")
def chat():
    return render_template("chat.html")
@app.route("/index.html")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
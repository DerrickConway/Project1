from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def HomePage():
    return render_template("HomePage.html")

@app.route("/post_user",methods=["POST"])
def post_user():
    return render_template("HomePage.html")



if __name__ == '__main__':
    app.run()

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/hi")
def index():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template("index.html",name=name,age=age)


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        if username == password:
            return "Successfully logged in!"
        else:
            return "Incorrect username/password"

if __name__ == "__main__":
    app.run(use_reloader=True)
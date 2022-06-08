from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome to home page !"	# notice the 2 new named arguments!

@app.route('/play')
def play():
    return render_template("Playground.html",repeat=3)

@app.route("/play/<int:number>")
def viewBox(number):
    return render_template("repeatboxs.html",repeat=number)


@app.route("/play/<int:number>/<color>")
def changecolor(number,color):
    return render_template("changeColor.html",repeat=number,mycolor= color)





if __name__=="__main__":
    app.run(debug=True)


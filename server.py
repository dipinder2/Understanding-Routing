from flask import Flask,render_template
app = Flask(__name__) 
app1 = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World" 


@app.route('/dojo')
def dojo():
    return "Dojo" 


@app.route('/say/<string:name>')
def sayName(name):
    return f"Hi {name}!" 


@app.errorhandler(404)
def nonDefinedRoutes(e):
    return "Sorry! No response. Try again"


@app.route('/repeat/<int:times>/<string:word>')
def sayWordMultipleTimes(times,word):
    return f"{word}\n"*times 

if __name__=="__main__":   
    app.run(debug=True) 


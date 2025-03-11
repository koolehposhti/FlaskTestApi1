from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/api/greet' , methods = ['GET'] )
def greetings():
    return jsonify({"Message":"This is an API Test"})


if __name__ == "__main__" :
    app.run(debug = True)

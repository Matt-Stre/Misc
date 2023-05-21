from flask import Flask, render_template, request, redirect
from calculator import calculate







app = Flask(__name__)

@app.route("/")
def home():
    dropdown = ['+', '-', '*', '/']
    return render_template('index.html', dropdown=dropdown)


@app.route("/", methods =["POST", "GET"])
def op():
    a=int(request.form.get("a_value", type=int))
    b=int(request.form.get("b_value", type=int))
    #operation = request.form.get("op_value")
    operation = request.form.get("dropdown")
    dropdown = ['+', '-', '*', '/']
    result =  "Result: " + str(calculate(a,b,operation))
    return render_template('index.html', result=result, dropdown=dropdown)













if __name__ == "__main__":
    app.run(debug=True)
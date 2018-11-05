from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def show_home():
    return render_template("index.html", result='unknown yet')

@app.route('/calculate_result')
def calculate_result():
  a = int(request.args.get('val1'))
  b = int(request.args.get('val2'))
  return jsonify({"result":a+b})

if __name__ == "__main__":
    app.run(debug=True)

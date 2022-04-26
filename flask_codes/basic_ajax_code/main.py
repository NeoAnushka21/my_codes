from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        todo = request.form.get("todo")
        print(todo)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)

from flask import Flask

app = Flask(__name__)

notes = {}

@app.route('/notes', methods = {"Get", "Post"})
def hello:
if request.method == "Get":
    return notes

if request.method == "Post":
    data = request.getjson()
    notes.update(data)
    return notes

app.run(host='127.0.0.1', port=8080, debug=True)

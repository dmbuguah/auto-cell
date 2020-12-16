import os
from flask import Flask
from auto_cell import get_programming_language

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    question = 'Your favorite random programming language? '
    page = '<html><body><h1>'
    page += question
    page += get_programming_language()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))

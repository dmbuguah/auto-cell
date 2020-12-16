import os
from flask import Flask
from awe_pro import auto_cell

app = Flask(__name__)

@app.route("/")
def get_favorite_programming_language():
    question = 'Your favorite random programming language? '
    page = '<html><body><h1>'
    page += question
    page += auto_cell.get_programming_language()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))

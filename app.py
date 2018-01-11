from flask import Flask, render_template
from random import choice
app = Flask(__name__)


@app.route('/')
def index():
    quotes = [
        'No pain, no gain',
        'Love yourself. It is important to stay positive because beauty comes from the inside out.',
        'Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.',
        'Let us always meet each other with smile, for the smile is the beginning of love.'
    ]
    quote_content = choice(quotes)
    return render_template("index.html", quote_content=quote_content)

if __name__ == '__main__':
  app.run(debug=True)

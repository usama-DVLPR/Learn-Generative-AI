from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/pass/<int:score>')
def pass_page(score):
    return f"You are passed with {score}"

@app.route('/fail/<int:score>')
def fail_page(score):
    return f"You are failed with {score}"

@app.route('/success/<int:score>')
def success_with_score(score):
    result = ''
    if score >= 50:
        redirect(url_for('pass_page', score=score))

    else:
        redirect(url_for('fail_page', score=score))
    return "pleas enter valid score"




if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        total_score = 0
        total_score += float(request.form['Science'])
        total_score += float(request.form['Math'])
        total_score += float(request.form['English'])
        total_score += float(request.form['History'])

        if total_score >= 200:
            return redirect(url_for('success', score=total_score))
        else:
            return redirect(url_for('fail', score=total_score))

    return render_template('index.html')

@app.route('/success/<float:score>')
def success(score):
    return render_template('result.html', result='Passed', score=score)

@app.route('/fail/<float:score>')
def fail(score):
    return render_template('result.html', result='Failed', score=score)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

# Admin dashboard
@app.route('/')
def admin():
    return render_template('admin.html')

# Active users by date
@app.route('/active')
def active():
    return render_template('active.html')

@app.route('/subject')
def subject():
    return render_template('subject.html')

@app.route('/difficulty')
def difficulty():
    return render_template('difficulty.html')

@app.route('/topic')
def topic():
    return render_template('topic.html')


# Student dashboard with dynamic username
@app.route('/student/<username>')
def student(username):
    return render_template('student.html', username=username)

if __name__ == '__main__':
    app.run(port=8080, debug=True)

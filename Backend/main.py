from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('test.html')

# Note the change from POST to GET since the form method is GET
@app.route('/page2')
def page2():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)

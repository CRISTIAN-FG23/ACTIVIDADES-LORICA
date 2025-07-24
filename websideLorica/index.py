from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/acercade')
def acercade():
    return render_template('acercade.html')



if __name__ == '__main__':
    app.run(debug=True)

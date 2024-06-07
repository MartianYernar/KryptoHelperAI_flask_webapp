from flask import Flask, render_template, request
# import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/next_page')
def next_page():
    return render_template('next_page.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

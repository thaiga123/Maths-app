from flask import Flask, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('images', filename)

@app.route('/scripts/<filename>')
def scripts(filename):
    return send_from_directory('scripts', filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adtn_1')
def adtn_1():
    return render_template('adtn-p1.html')

@app.route('/adtn_2')
def adtn_2():
    return render_template('adtn-p2.html')

@app.route('/adtn_3')
def adtn_3():
    return render_template('adtn-p3.html')

@app.route('/adtn_4')
def adtn_4():
    return render_template('adtn-p4.html')

@app.route('/adtn_5')
def adtn_5():
    return render_template('adtn-p5.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
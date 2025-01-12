from flask import Flask, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)


#ADDITION

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



#SUBTRACTION

@app.route('/sub_1')
def sub_1():
    return render_template('sub-p1.html')

@app.route('/sub_2')
def sub_2():
    return render_template('sub-p2.html')

@app.route('/sub_3')
def sub_3():
    return render_template('sub-p3.html')

@app.route('/sub_4')
def sub_4():
    return render_template('sub-p4.html')

@app.route('/sub_5')
def sub_5():
    return render_template('sub-p5.html')



#MULTIPLICATION

@app.route('/multi_1')
def multi_1():
    return render_template('multi-p1.html')

@app.route('/multi_2')
def multi_2():
    return render_template('multi-p2.html')

@app.route('/multi_3')
def multi_3():
    return render_template('multi-p3.html')

@app.route('/multi_4')
def multi_4():
    return render_template('multi-p4.html')

@app.route('/multi_5')
def multi_5():
    return render_template('multi-p5.html')


#DIVISION

@app.route('/div_1')
def div_1():
    return render_template('div-p1.html')

@app.route('/div_2')
def div_2():
    return render_template('div-p2.html')

@app.route('/div_3')
def div_3():
    return render_template('div-p3.html')

@app.route('/div_4')
def div_4():
    return render_template('div-p4.html')

@app.route('/div_5')
def div_5():
    return render_template('div-p5.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is" + " " + str(squared) + " " + "<a href='"+ url_for('square', number=number+1) +"'>Square of " + str(number+1) + "</a>"
    return line

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
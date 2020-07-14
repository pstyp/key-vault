from flask import Flask, render_template, url_for, abort

app = Flask(__name__)

@app.route('/images/<path:filename>')
def images(filename):
    return render_template('images.html', filename=filename)


@app.route('/videos/<path:filename>')
def videos(filename):
    if not url_for('static', filename=filename):
        abort(404)
    return render_template('videos.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)

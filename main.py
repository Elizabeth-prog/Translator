from translator import translate
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["post", "get"])
def translator():
    if request.method == 'POST':
        return render_template('translator.html', my_string=translate(
            request.form.get('trans'),
            request.form.get('from'),
            request.form.get('to')))
    return render_template('translator.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    nome = request.form['nome']

    # Salvar o nome no arquivo file.txt
    with open('static/file.txt', 'a') as file:
        file.write(nome + '\n')

    return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('return.html')

if __name__ == '__main__':
    app.run(debug=True)

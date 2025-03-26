from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

def hash_string(input_string, algorithm):
    if algorithm == 'sha1':
        return hashlib.sha1(input_string.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(input_string.encode()).hexdigest()
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    hashed_output = None
    input_string = None
    if request.method == 'POST':
        input_string = request.form['input_string']
        algorithm = request.form['algorithm']
        hashed_output = hash_string(input_string, algorithm)
    return render_template('index.html', hashed_output=hashed_output, input_string=input_string)

if __name__ == '__main__':
    app.run(debug=True)
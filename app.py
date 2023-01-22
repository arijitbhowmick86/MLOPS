from flask import Flask

app = Flask(__name__)

@app.route('/ping/<name>', methods=['GET'])
def test_connection(name):
    return f'Welcome Mr. {name} !'


# docker build -t flask_app .
# docker run -d -p 8000:5000 flask_app
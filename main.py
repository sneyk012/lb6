import random
from flask import Flask


app = Flask(__name__)


@app.route('/')
def health_check():
    if random.random() > 0.2:
        return 'it is working', 200
    else:
        return 'it is not working', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
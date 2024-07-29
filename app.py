from flask import Flask, render_template
import os

app = Flask(__name__)

counter = 0

@app.route('/')
def index():
    pod_name = os.environ.get('POD_NAME')
    node_name = os.environ.get('NODE_NAME')
    return render_template('index.html', pod_name=pod_name, node_name=node_name)

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')
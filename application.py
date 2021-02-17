from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Updated World. This is test from Faiz!"

if __name__ == '__main__':
    app.run()

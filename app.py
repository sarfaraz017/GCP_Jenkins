from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins CI/CD Pipeline on GCP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

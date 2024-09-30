from flask import Flask 

app = Flask(__name__)

@app.route ("/")

def index():
    return "What is up baby girl?"

if __name__ == "__main__":
    app.run(debug=True)
    
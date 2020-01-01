from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there!"

@app.route('/v1.0/test', methods=['GET','POST'])
def test():
    return "TEST HIT!"



if __name__ == '__main__':
    app.run(debug=True)
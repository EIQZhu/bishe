from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/user')
def user():
    return render_template('index.html')
    
@app.route('/page2.html')
def page2():
    return render_template('page2.html')    
    
    
@app.route('/userdata', methods=['POST'])
def login():
    json = request.json
    print('recv:', json)
    return json


if __name__ == '__main__':
    app.run(debug=True)


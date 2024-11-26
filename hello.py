from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用跨域支持

@app.route('/user')
def user():
    return render_template('page1.html')
    
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


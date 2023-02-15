from flask import *
import random

app = Flask(__name__)

@app.route('/random/<int:num>',methods = ['GET'])
def get_random(num):
    arr =[]
    if num >= 0 and num <= 1000:
        for i in range(num):
            n = random.randint(1,1000)
            if n not in arr:
                arr.append(n)
    return json.dumps(arr)

if __name__ == ('__main__'):
    app.run(debug=True)
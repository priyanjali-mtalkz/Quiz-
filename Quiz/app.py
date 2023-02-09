from flask import *
from controller import *
from model.schema import Schema
import pymongo
import time
from flask import request,render_template,redirect,url_for,jsonify

app = Flask(__name__)


obj = Schema()
arr = []
user_answers = []
score = 0
start_time = 0
end_time = 0
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Quiz']        
coll = db['Question']
user_name = None
mobile = None
level = None

@app.route('/',methods=['GET','POST'])
def home():
    return  "Welcome"


@app.route('/users',methods = ['GET','POST'])
def register():
    register.start_time = time.time()
    print(register.start_time)
    try:
        if request.method == 'POST':
            return render_template("signup.html")
        elif request.method == 'GET':
            return render_template("signup.html")
    except Exception as e:
        print(e)

@app.route('/level/quiz',methods = ['GET','POST'])
def user_level():
    user_level.user_name = request.form.get("fname")
    print(user_level.user_name)
    user_level.mobile = request.form.get('mobile')
    print(user_level.mobile)
    return render_template("level.html")

@app.route('/play/quiz',methods = ['GET','POST'])
def game():
    game.level = request.form.get('level')
    print(game.level)
    for quest in coll.find({'Level':game.level}):
        #print(quest['questions'])
        # coll1.aggregate([{$sample:{size:1}}])
        return render_template("quiz.html",question = quest['questions'])


@app.route('/submit/quiz',methods = ['POST','GET'])
def submit():
    ans = 0
    print(game.level)
    l = game.level
    for ques in coll.find({'Level':l}):
        q = ques['questions']
        print((q[0]['q_id']))
        try:
            for dic in q:
                print("hello")
                dic['q_id'] = str(dic['q_id'])
                user_answer = request.form.get(dic['q_id'])
                user_answer = user_answer[:1]
                #print(user_answer)
                user_answers.append(user_answer)
                correct_ans = dic['answer']
                #print(correct_ans)
                if(user_answer.startswith(correct_ans)):
                    ans = ans + 1
                #print(ans)
            submit.score = str(ans)
            return render_template("score.html",score = submit.score)
        except Exception as e:
            print("---ERROR----",e)
        return jsonify()
    

        
@app.route('/play/again',methods = ['GET','POST'])
def play_again():
    play_again.end_time = time.time()
    #print(end_time)
    if request.method == 'POST':
        try:
            if (request.form.get('choice') == "YES"):
                return redirect(url_for('user_level'),code = 302)
            else:
                return render_template("thankyou.html")
        except Exception as e:
            print("----ERROR------",e) 
        return jsonify()
    return jsonify({"Status" : "Thankyou"})
            

@app.route('/users/get/details')
def data():
    try:
        time_taken = play_again.end_time-register.start_time
        user_data = {}
        arr1 = []
        data1 = "User Name"
        user_data[data1] = user_level.user_name
    

        data2 = "Mobile"
        user_data[data2] = user_level.mobile

        data3 = "Level"
        user_data[data3] = game.level

        data4 = "Score"
        user_data[data4] = submit.score

        data5 = "Timetaken"
        user_data[data5] = time_taken

        data6 = "User answers"
        user_data[data6] = user_answers

        arr1.append(user_data)
        user_data = {}

        return obj.user_add_details(arr1)
    except Exception as e:
        print("error in data function",e)

    return jsonify()


if __name__ == "__main__":
    app.run(debug=True)




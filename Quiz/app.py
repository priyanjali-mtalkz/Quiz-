from flask import Flask
from controller import *
from model.schema import Schema
import pymongo
import time
from flask import request,render_template,redirect,url_for,jsonify
import random
from model.configure import configure
from datetime import datetime

app = Flask(__name__)

obj = Schema()

obj1 = configure()
arr = []
user_answers = []
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Quiz']        
coll = db['Question']
user_questions = []


@app.route('/',methods=['GET','POST'])
def register():
    try:
        if request.method == 'POST':
            return render_template("signup.html")
        elif request.method == 'GET':
            return render_template("signup.html")
    except Exception as e:
        print(e)


@app.route('/level/quiz',methods = ['GET','POST'])
def user_level():
    if request.method == 'POST':
        user_name = request.form.get("fname")
        print(user_name)
        obj1.setName(user_name)
        mobile = request.form.get('mobile')
        print(mobile)
        obj1.setMobile(mobile)
        return render_template("level.html")
    else:

        return render_template("level.html")
# @app.route('/play/quiz',methods = ['GET','POST'])
# def game():
#     game.level = request.form.get('level')
#     print(game.level)
#     for quest in coll.find({'Level':game.level}):
#         q = quest['questions']
#         game.q_rand = random.sample(q,5)
#         #print(quest['questions'])
#         # coll1.aggregate([{$sample:{size:1}}])
#         return render_template("quiz.html",question = game.q_rand)


# @app.route('/play/quiz',methods=['GET','POST'])
# def game():
#     start_time = time.time()
#     obj1.setStartTime(start_time)
#     print(start_time)
#     level = request.form.get('level')
#     obj1.setLevel(level)
#     quest = [i for i in coll.find({'Level':level}) if i not in user_questions]
#     for quest in coll.find({'Level':level}).limit(5):
#         q = quest['questions']
#         game.q_rand = random.sample(q,5)
#         return render_template("quiz.html",question = game.q_rand)

@app.route('/play/quiz',methods=['GET','POST'])
def game():
    start_time = time.time()
    obj1.setStartTime(start_time)
    print(start_time)
    level = request.form.get('level')
    obj1.setLevel(level)
    quest = [i for i in coll.find({'Level':level}) if i not in user_questions]
    for quest in coll.find({'Level':level}).limit(5):
        q = quest['questions']
        game.q_rand = random.sample(q,5)
        return render_template("quiz.html",question = game.q_rand)


@app.route('/submit/quiz',methods = ['POST','GET'])
def submit():
        ans = 0
        print(obj1.getLevel())
        try:
            for dic in game.q_rand:
                print("hello")
                print(type(dic['date']))
                dic['date'] = datetime.strptime(
                        "2023-09-01 ",
                        "%Y-%m-%d ")
                dic['date'] = str(dic['date'])
                if(dic['date'] > '2023-02-01 00:00:00'):
                    dic['q_id'] = str(dic['q_id'])
                    user_question = int(dic['q_id'])
                    user_questions.append(user_question)
                    user_answer = request.form.get(dic['q_id'])
                    user_answer = user_answer[:1]
                    #print(user_answer)
                    user_answers.append(user_answer)
                    correct_ans = dic['answer']
                    #print(correct_ans)
                    if(user_answer.startswith(correct_ans)):
                        ans = ans + 1
                    print(ans)
                score = str(ans)
                obj1.setScore(score)
                
            return render_template("score.html",score = score)
        except Exception as e:
            print("ERROR : ",e)
        return jsonify()
    
@app.route('/get/filtered/questions')
def get_questions():
    level = "EASY"
    try:
        for ques in coll.find({'Level':level}):
            q = ques['questions']
            for dic in q:
                dic['date'] = str(dic['date'])
                if(dic['date'] > '2023-02-14'):
                    print(dic['question'])
    
    except Exception as e:
        print(e)
    return jsonify({"Status":"successful"})


@app.route('/play/again',methods = ['GET','POST'])
def play_again():
    end_time = time.time()
    obj1.setEndTime(end_time)
    print(end_time)
            
    if request.method == 'POST':
        try:
            if (request.form.get('choice') == "YES"):
                return redirect(url_for('user_level'),code = 302)
            else:
                return render_template("thankyou.html")
                # return redirect(url_for('data'),code = 302)
        except Exception as e:
            print("----ERROR------",e) 
            return jsonify()
    return jsonify({"Status" : "Thankyou"})

            
@app.route('/users/get/details')
def data():
    try:
        time_taken = obj1.getEndTime() - obj1.getStartTime()
        user_data = {}
        arr1 = []
        data1 = "User Name"
        user_data[data1] = obj1.getName()
    

        data2 = "Mobile"
        user_data[data2] = obj1.getMobile()

        data3 = "Level"
        user_data[data3] = obj1.getLevel()

        data4 = "Score"
        user_data[data4] = obj1.getScore()

        data5 = "Timetaken"
        user_data[data5] = "%.2f" %time_taken

        #today = date.today()
        dateToday = datetime.now()

        data6 = "Date"

        user_data[data6] = dateToday


        data7 = "User answers"
        user_data[data7] = user_answers

        data8 = "User questions"
        user_data[data8] = user_questions

        arr1.append(user_data)
        user_data = {}

        return obj.user_add_details(arr1)
    except Exception as e:
        print("error in data function",e)

    return jsonify()


if __name__ == "__main__":
    app.run(debug=True)




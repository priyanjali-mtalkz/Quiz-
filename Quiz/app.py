from flask import Flask
from model.schema import Schema
import pymongo
import time
from flask import request,render_template,redirect,url_for,jsonify
import random
from model.configure import configure
from datetime import datetime
import test
import redis
import json
from datetime import timedelta

app = Flask(__name__)

obj = Schema()
obj1 = configure()

arr = []

cache = redis.StrictRedis(host='localhost',port=6379,decode_responses = True)
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Quiz']        
coll = db['Question']
user_questions = []

def check_ans(l1, l2):
   for i in range(min(len(l1), len(l2))):
       if l1[i] != l2[i]:
           return False
   return len(l1) == len(l2)

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



@app.route('/play/quiz',methods=['GET','POST'])
def game():
    game.user_answers = []
    start_time = time.time()
    obj1.setStartTime(start_time)
    print(start_time)
    level = request.form.get('level')
    obj1.setLevel(level)
    quest = [i for i in coll.find({'Level':level}) if i not in user_questions]
    for quest in coll.find({'Level':level}).limit(5):
        # print(quest)
        q = quest['questions']
        #print(type(q))
        new_q = list(filter(test.afterDate, q))        
        #print(new_q)
        game.q_rand = random.sample(q,5)
        # print(game.q_rand[0])
        # print(game.q_rand[1])
        # print(game.q_rand[2])
        # print(game.q_rand[3])
        # print(game.q_rand[4])
        #game.q_rand = random.sample(new_q,len(new_q) if len(new_q)<5 else 5)
        #return render_template("quiz.html",question = game.q_rand)    
        return render_template("q1.html",question=game.q_rand[0],user_id =  obj1.getMobile())
    return jsonify()

@app.route('/q2',methods = ['POST'])
def qu():
    user_answer = request.form.to_dict('ans')
    # user_answer = user_answer[:1]
    ans = list(user_answer.values())
    ans = ans[0]
    user_ans = ans[:1]
    print(user_ans)
    game.user_answers.append(user_ans)
    return render_template("q2.html",question=game.q_rand[1],user_id= obj1.getMobile())

@app.route('/q3',methods = ['POST'])
def que():
    user_answer = request.form.to_dict('ans')
    # user_answer = user_answer[:1]
    ans = list(user_answer.values())
    ans = ans[0]
    user_ans = ans[:1]
    print(user_ans)
    game.user_answers.append(user_ans)
    return render_template("q3.html",question=game.q_rand[2],user_id= obj1.getMobile())

@app.route('/q4',methods = ['POST'])
def ques():
    user_answer = request.form.to_dict('ans')
    # user_answer = user_answer[:1]
    ans = list(user_answer.values())
    ans = ans[0]
    user_ans = ans[:1]
    print(user_ans)
    game.user_answers.append(user_ans)
    return render_template("q4.html",question=game.q_rand[3],user_id= obj1.getMobile())

@app.route('/q5',methods = ['POST'])
def quest():
    user_answer = request.form.to_dict('ans')
    # user_answer = user_answer[:1]
    ans = list(user_answer.values())
    ans = ans[0]
    user_ans = ans[:1]
    print(user_ans)
    game.user_answers.append(user_ans)
    return render_template("q5.html",question=game.q_rand[4],user_id= obj1.getMobile())
    


# @app.route('/home')
# def optionc():
#     # for q in coll.aggregate([{ '$match' : {"$and":[{ 'Level' : 'EASY'},{'questions': { '$elemMatch': { 'answer': "C"} }}]} }, { '$unwind' : '$questions' }, { '$project' : { '_id' : 1, 'Level' : 1, 'questions.answer' : 1} }]):
#     for q in coll.find({'Level': 'EASY','questions': { '$unwind' : '$questions' }, { '$elemMatch': { 'answer': "C"}}} ):
#         print(q)
#     return jsonify()


@app.route('/submit/quiz',methods = ['POST','GET'])
def submit():
        cache.flushall()
        a = 0
        user_answer = request.form.to_dict('ans')
        # user_answer = user_answer[:1]
        ans = list(user_answer.values())
        ans = ans[0]
        user_ans = ans[:1]
        print(user_ans)
        game.user_answers.append(user_ans)
        correct_answers = []
        print(obj1.getLevel())
        
        try:
            for dic in game.q_rand:
                print("1")
                dic['q_id'] = str(dic['q_id'])
                user_question = int(dic['q_id'])
                print("21")
                user_questions.append(user_question)
                correct_ans = dic['answer']
                correct_answers.append(correct_ans)
                print("321")
            print((correct_answers))
            print(type(game.user_answers))
            cache.set(obj1.getMobile(),'user_ans')
            cache.expire('user_ans',timedelta(seconds = 30))
            for i in range(len(game.user_answers)):
                cache.lpush('user_ans',game.user_answers[i])
            print("hello")
            #if(user_answers.startswith(correct_ans)):
            for i in range(0,5):
                if(check_ans(game.user_answers[i],correct_answers[i])):
                    a = a + 1
                print(a) 

            score = str(a)                
            obj1.setScore(score)
            cache.set(obj1.getMobile(),score)
            return render_template("score.html",score = score,user_id= obj1.getMobile())
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


@app.route('/add')
def add():
    try:
        time_taken = obj1.getEndTime() - obj1.getStartTime()
        user_data = {}
        arr1 = []
        data1 = "Mobile"
        user_data[data1] = obj1.getMobile()
        print("111111")
        data2 = "User answers"
        user_data[data2] = cache.lrange('user_ans',0,-1)
        print("----------")
        
        data3 = "Score"
        user_data[data3] = cache.get(obj1.getMobile())
        print("!!!!!!!!!!!!!!!!!!!!")

        data4 = "Timetaken"
        user_data[data4] = "%.2f" %time_taken

        dateToday = datetime.now()
        data5 = "Date"
        user_data[data5] = dateToday

        arr1.append(user_data)
        user_data = {}
        cache.expire(obj1.getMobile(),timedelta(seconds = 30))
        return obj.user_add_details(arr1)
    except Exception as e:
        print("error in data function",e)

    return jsonify()

if __name__ == "__main__":
    app.run(debug=True)




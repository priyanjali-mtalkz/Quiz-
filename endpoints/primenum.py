from flask import *
import math

app = Flask(__name__)
#program to print first n prime numbers
# @app.route('/prime/<int:num>',methods = ['GET'])
# def prime_num(num):
#     arr = []
#     for i in range(0,num+1):
#         prime = 0
#         if i == 0 or i == 1:
#             prime = 1
#         for x in range(0,1000):
#             if (x%i) == 0:
#                 prime = 1
#                 break

#         if prime == 0:
#             arr.append(x)

#     return json.dumps(arr)


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n)+2)):
        if(n%i)== 0:
            return False
        else:
            return True


@app.route('/prime/<int:num>',methods = ['GET'])
def prime_num(num):
    arr = []
    i = 2    
    if num >= 0 and num <= 1000:
        while(len(arr) < num):
            if isPrime(i):
                arr.append(i)   
            i += 1
    return json.dumps(arr)



if __name__ == ('__main__'):
    app.run(debug=True)
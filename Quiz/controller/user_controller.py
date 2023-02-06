from app import app
from model.schema import Schema

obj = Schema()
@app.route('/users/register')
def register():
    #return({"Status" : "This is the signup page"})
    return obj.user_signup()

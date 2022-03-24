from flask import Blueprint, request, redirect, render_template

users = {
    "admin":{"password":'123'},
    "suraj":{"password":'456'}
}
 
routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/userlogin', methods = ['POST'] )
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    print(username)
    print(password)
    if not username or not password:
        return render_template('index.html')
    if username in users:
        if users[username]['password'] != password:
            return '<h1 style="color:red">Unautherised User</h1>'
        else:
            return '<h1 style="color:green"> Welcome ' +username+ '</h1>'
    else:
        return '<h1 style="color:red">Invalid User/Password</h1>'
    
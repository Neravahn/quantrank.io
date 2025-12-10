from flask import Flask, render_template, request, session, redirect
from auth.emailAuth import send_otp
from auth.user import check_email, check_username
from auth.save_user import save


app = Flask(__name__)
app.secret_key = "idk_what_secretkey_to_use"

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        if check_username(username):
            return render_template('signup.html', error = "USERNAME already in use")
        
        elif check_email(email):
            return render_template('signup.html', error= "E-MAIL already in use")
        
        otp = send_otp(email)
        if otp is None:
            return render_template('signup.html', error= "OTP cannot be sent")
        session['username'] = username
        session['real_otp'] = otp
        session['email'] = email
        session['name'] = name
        session['password'] = password
        return redirect('verify')
    return render_template('signup.html')

@app.route('/verify', methods = ['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']
        real_otp = session.get('real_otp')
        name = session.get('name')
        email = session.get('email')
        password = session.get('password')
        username = session.get('username')
        if user_otp == real_otp:
            save(name, username, email, password)
            print( 'success' )
            return redirect('login')
        else:
            return render_template('verify.html', error = 'Enter correct OTP')
    

    return render_template('verify.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, session, redirect, jsonify
from auth.emailAuth import send_otp
from auth.user import check_email, check_username
from auth.save_user import save
from auth.login import verify_user
from questionImport import check
from statsFolder.userStats import stats_save, update_points, update_stats
from statsFolder.getUserDetails import getUserData
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
            return render_template('auth/signup.html', error = "USERNAME already in use")
        
        elif check_email(email):
            return render_template('auth/signup.html', error= "E-MAIL already in use")
        
        otp = send_otp(email)
        if otp is None:
            return render_template('auth/signup.html', error= "OTP cannot be sent")
        
        session['username_signup'] = username
        session['real_otp_signup'] = otp
        session['email_signup'] = email
        session['name_signup'] = name
        session['password_signup'] = password
        return redirect('verify')
    return render_template('auth/signup.html')

@app.route('/verify', methods = ['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']
        real_otp = session.get('real_otp_signup')
        name = session.get('name_signup')
        email = session.get('email_signup')
        password = session.get('password_signup')
        username = session.get('username_signup')


        if user_otp == real_otp:
            save(name, username, email, password)
            stats_save(username)
            session.pop('username_signup', None)
            session.pop('email_signup', None)
            session.pop('password_signup', None)
            session.pop('real_otp_signup', None)
            session.pop('name_signup', None)
            return redirect('login')
        else:
            return render_template('auth/verify.html', error = 'Enter correct OTP')
    

    return render_template('auth/verify.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        verified = verify_user(username, password)

        if verified == True:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('auth/login.html', error= 'Invalid Credentials')
        
    return render_template('auth/login.html')

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect('/login')
    
    username = session.get('username')
    data = getUserData(username)
    easy = data[0]
    medium = data[1]
    hard = data[2]
    
    return render_template('dashboard.html', easy = easy, medium = medium, hard = hard)

@app.route('/questions', methods = ['GET', 'POST'])
def questions():
    if request.method== 'POST':
            data = request.get_json()
            topic = data.get("topic")
            difficulty = data.get('difficulty')
            session['difficulty'] = difficulty
            question, options, answer = check(difficulty, topic)
            option1 = options[0]
            option2 = options[1]
            option3 = options[2]
            option4 = options[3]
            session['option1'] = option1
            session['option2'] = option2
            session['option3'] = option3
            session['option4'] = option4
            session['answer'] = answer
            html = render_template("questions.html",
                                    question = question, 
                                    option1 = option1,
                                    option2 = option2,
                                    option3 = option3,
                                    option4 = option4
                                    )
            return jsonify({"html": html})
    return render_template('question_dash.html')

@app.route('/check_answers', methods=['POST'])
def check_answers():
    option1 = session.get('option1')
    option2 = session.get('option2')
    option3 = session.get('option3')
    option4 = session.get('option4')
    answer = session.get('answer')
    username = session.get('username')
    difficulty = session.get('difficulty')

    data = request.get_json()

    
    selected = int(data.get('selected'))
    if selected == 1:
        op_sel = option1
    elif selected == 2:
        op_sel = option2
    elif selected == 3:
        op_sel = option3
    elif selected == 4:
        op_sel = option4


    if op_sel == answer:
        update_stats(username, difficulty)
        update_points(username, 1)
        return jsonify({"message" : "correct"})
    else:
        update_points(username, -1)
        return jsonify({"message" : "wrong"})



if __name__ == "__main__":
    app.run(debug=True)
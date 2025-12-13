from flask import Flask, render_template, request, session, redirect, jsonify
from auth.emailAuth import send_otp
from auth.user import check_email, check_username
from auth.save_user import save
from auth.login import verify_user
from questionImport import check


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
        session['username'] = username
        session['real_otp'] = otp
        session['email'] = email
        session['name'] = name
        session['password'] = password
        return redirect('verify')
    return render_template('auth/signup.html')

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
            return render_template('auth/verify.html', error = 'Enter correct OTP')
    

    return render_template('auth/verify.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        verified = verify_user(username, password)

        if verified == True:
            return redirect('/dashboard')
        else:
            return render_template('auth/login.html', error= 'Invalid Credentials')
        
    return render_template('auth/login.html')

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/questions', methods = ['GET', 'POST'])
def questions():
    if request.method== 'POST':
            data = request.get_json()
            topic = data.get("topic")
            difficulty = data.get('difficulty')
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
                                    answer = answer,
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
        print('correct answer')
    else:
        print('wrong answer')
    
    return jsonify({"correct": selected == answer, "correct_answer": answer})



if __name__ == "__main__":
    app.run(debug=True)
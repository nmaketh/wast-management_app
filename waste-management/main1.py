import json
from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user

from flask_mail import Mail



#db connection
local_server=True
app=Flask(__name__)
app.secret_key='sjbit'


login_manager=LoginManager(app)
login_manager.login_view='login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
    
    
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/msw'
db=SQLAlchemy(app)



    
#db tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
   # address=db.Column(db.String(50))
    password=db.Column(db.String(1000))
    
class Complaints(db.Model):
    cid=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    message=db.Column(db.String(50))
    date=db.Column(db.String(50),nullable=False)
    image=db.Column(db.String(50))
    
    
# to pass endpoints
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/home')
@login_required
def home():
        return render_template('home.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)

        new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")

        # this is method 2 to save data in db
        # newuser=User(username=username,email=email,password=encpassword)
        # db.session.add(newuser)
        # db.session.commit()
        flash("Signup Succes Please Login","success")
        return render_template('login.html')

          

    return render_template('signup.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')    


    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Succesful","warning")
    return redirect(url_for('login'))   



@app.route('/prcomplaint')
@login_required
def prcomplaint():
    c_email=current_user.email
    comp=db.engine.execute(f"SELECT * FROM `complaints` WHERE email='{c_email}'")
    return render_template('prcomplaint.html',comp=comp)

@app.route('/Complaint',methods=['POST','GET'])
@login_required
def Complaint():
    if request.method =="POST":
        email=request.form.get('email')
        message=request.form.get('message')
        date=request.form.get('date')
        image=request.form.get('image')
        query=db.engine.execute(f"INSERT INTO `complaints` (`email`,`message`,`date`,`image`) VALUES ('{email}','{message}','{date}','{image}')")




    flash("Complaint Submited Thank you!","primary")


    return render_template('Complaint.html')




@app.route('/areadetails')
@login_required
def area():
    if not User.is_authenticated:
        return render_template('login.html')
    return render_template('areadetails.html')

@app.route("/edit/<string:cid>",methods=['POST','GET'])
@login_required
def edit(cid):
    posts=Complaints.query.filter_by(cid=cid).first()
    if request.method=="POST":
        email=request.form.get('email')
        message=request.form.get('message')
        date=request.form.get('date')
        image=request.form.get('image')
        query= db.engine.execute(f"UPDATE `complaints` SET `email` = '{email}', `meassage` = '{message}', `date` = '{date}', `image` = '{image}',   WHERE `complaints`.`cid` = {cid}")
        flash("Slot is Updates","success")
        return redirect('/complaint')
    
    return render_template('edit.html',query=query)

app.run(debug=True)

#
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from models import User, Collection, Complaints, Schedule

@app.route('/')
def index():
    return render_template('index.html')

# Rest of your routes...

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email Already Exist", "warning")
            return render_template('/signup.html')

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup Successful. Please Login", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Successful", "success")
            return redirect(url_for('index'))

        else:
            flash("Invalid credentials", "danger")

    return render_template('login.html')
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Succesful","warning")
    return redirect(url_for('login'))   

@app.route('/admin')
@login_required
def admin():
    system = {
        'uptime': 'Your system uptime value',
        'response_time': 'Your system response time value'
    }
    collections = Collection.query.all()  # Assuming you have a Collection model
    return render_template('admin.html', system=system, collections=collections)
    
@app.route('/schedule', methods=['POST', 'GET'])
@login_required
def schedule():
    if request.method == 'POST':
        email=request.form.get('email')
        message=request.form.get('message')
        date=request.form.get('date')
        image=request.form.get('image')
        new_schedule = Schedule(email=email, message=message, date=date, image=image)
        db.session.add(new_schedule)
        db.session.commit()
        flash("Schedule created successfully", "success")
        return redirect(url_for('admin'))
    return render_template('schedule.html')

@app.route('/schedules')
@login_required
def schedules():
    schedules = Schedule.query.all()
    return render_template('schedules.html', schedules=schedules)

@app.route('/areadetails')
@login_required
def area():
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
        posts.email = email
        posts.message = message
        posts.date = date
        posts.image = image
        db.session.commit()
        flash("Slot is Updates","success")
        return redirect('/complaint')

    return render_template('edit.html',query=posts)
@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    if request.method == 'POST':
        # Handle the form submission
        complaint_text = request.form.get('complaint')
        # Save the complaint to the database or do something else with it
        # ...
        flash('Your complaint has been submitted', 'success')
        return redirect(url_for('complaint'))
    # If the method is GET, render the complaint page
    return render_template('complaint.html')
app.run(debug=True)
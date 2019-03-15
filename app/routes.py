from flask import render_template, flash, redirect, url_for, request
from app.forms import RegistrationForm, LoginForm
from app import app, db, bcrypt
from app.models import User, Post
posts = [
    {
     'author': 'Moises Montero',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'April 20, 2018'
    },
    {
     'author': 'Kevin Montero',
     'title': 'Blog Post 2',
     'content': 'Second post content',
     'date_posted': 'May 20, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='home')


@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/register', methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if request.method == 'POST':
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username= form.username.data, email= form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()


        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()
    if request.method == 'POST':
        if form.email.data == 'example@gmail.com' and form.password.data == '1234':
            flash('You have been Logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title='Login', form=form)

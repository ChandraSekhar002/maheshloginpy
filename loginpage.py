from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Npassword%40456@216.230.74.17/Loginpy'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secret key for session management
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Registration route
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password = generate_password_hash(password, method='scrypt', salt_length=8)
        
        "scrypt:32768:8:1$CorCJE2D$b86b1b752738ddbb5bff5bbe237a5a62df9f8a5213f5807a6acc03030896daa82e62aae262edc7b5baa24d59066dc0ca3740786e76ad703924795292e9fb21dd"
        
        # Check if the email is already registered
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address is already registered.', 'error')
        else:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            # Successful login
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            # Invalid login
            flash('Login failed. Please check your email and password.', 'error')

    return render_template('login.html')

# Home route
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()

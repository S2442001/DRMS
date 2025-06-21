from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# user model for victims/users and voulnteers/admin.
class User(db.Model, UserMixin):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), unique=True, nullable=False)
    password_hash=db.Column(db.String(100), nullable=False)
    role=db.Column(db.String(100), nullable=False, default='user') #user/admin

    sos_request=db.relationship('SOSRequest', backref='user', lazy=True)


    def set_password(self, password): 
        self.password_hash = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)



#sos request model for handling incoming request

class SOSRequest(db.Model):
    __tablename__='sos_requests'

    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location=db.Column(db.String(200), nullable=False)
    description=db.Column(db.Text, nullable=False)
    status=db.Column(db.String(120), default='Pending') #pending/resolved/rejected
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

# shelter model for handling shelter for users/victims

class Shelter(db.Model):
    __tablename__='shelters'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), nullable=False)
    capacity=db.Column(db.Integer, nullable=False)
    available_beds=db.Column(db.Integer, nullable=False)
    location=db.Column(db.String(200), nullable=False)


class Resource(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'water', 'food', 'medicine'
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(200), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
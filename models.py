from db import db
import datetime

class User(db.Model):
    __tablename__ = 'u' \
    'ser'

    User_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), unique=True, nullable=False)
    Password = db.Column(db.String(45), nullable=False)  # plain text (insecure)
    Create_id = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    role = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f'<User {self.Username}>'

class Destination(db.Model):
    __tablename__ = 'Destination'

    Destination_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(20), nullable=False)
    Place = db.Column(db.String(20), nullable=False)
    Type = db.Column(db.Enum('beach', 'hill', 'wildlife'), nullable=False)
    Description = db.Column(db.Text, nullable=True)
    Create_id = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return f'<Destination {self.Name}>'

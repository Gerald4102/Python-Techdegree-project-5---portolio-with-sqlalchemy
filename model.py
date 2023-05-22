from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///projects.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.DateTime)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    link = db.Column('GitHub_link', db.Text)

    def __repr__(self):
        return f'''Project Name:{self.title}
                Date: {self.date}
                Description: {self.description}
                Skills Learnt: {self.skills}
                GitHub Repo Link: {self.link}'''
    
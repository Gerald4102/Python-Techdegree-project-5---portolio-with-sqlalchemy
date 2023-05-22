from flask import (render_template, redirect,
                   url_for, request)
from model import Project, db, app
import datetime

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def create():
    if request.form:
        date = request.form['date']
        date = datetime.datetime.strptime(date, '%Y-%m')
        new_project = Project(
            title = request.form['title'],
            date = date,
            description = request.form['desc'],
            skills = request.form['skills'],
            link = request.form['github']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>')
def detail(id):
    return render_template('detail.html')


@app.route('/projects/<id>/edit')
def edit(id):
    pass


@app.route('/projects/<id>/delete')
def delete(id):
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
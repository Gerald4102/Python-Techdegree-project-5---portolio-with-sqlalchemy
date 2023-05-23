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
    proj = Project.query.get_or_404(id)
    date = datetime.datetime.strftime(proj.date, '%B %Y') 
    skills = proj.skills.split(',')
    return render_template('detail.html', project=proj, date=date, skills=skills)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    proj = Project.query.get_or_404(id)
    date_entry = datetime.datetime.strftime(proj.date, '%Y-%m')
    if request.form:
        proj.title = request.form['title']
        date = request.form['date']
        date = datetime.datetime.strptime(date, '%Y-%m') 
        proj.date = date
        proj.description = request.form['desc']
        proj.skills = request.form['skills']
        proj.link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=proj, date=date_entry)

@app.route('/projects/<id>/delete')
def delete(id):
    proj = Project.query.get_or_404(id)
    db.session.delete(proj)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')

# https://cdn.pixabay.com/photo/2016/11/29/13/14/attractive-1869761_1280.jpg
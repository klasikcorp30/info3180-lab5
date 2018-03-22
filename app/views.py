"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
#from flask_login import login_user, logout_user, current_user, login_required
#from forms import LoginForm
from models import UserProfile
from forms import AddProfile
from werkzeug.utils import secure_filename
import os
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')

filefolder = "app/static/uploads/" #url_for('uploads')#../ or ../../
@app.route('/profile',methods=['GET', 'POST'])
def get_profile():
    form = AddProfile()
    if request.method == 'POST' and form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(os.path.join( filefolder, filename))
        created_on = datetime.datetime.now().strftime('%A %d %B %Y')
        user = UserProfile(first_name=form.firstname.data,last_name=form.lastname.data, gender = form.gender.data,
        email = form.email.data, location = form.location.data,biography = form.biography.data, image = filename,created_on=created_on)
        db.session.add(user)
        db.session.commit()
        flash('New Profile Successfully Created')
        return redirect(url_for('get_profiles'))
    return render_template('profile.html',form=form)

@app.route('/profiles')
def get_profiles():
    users = UserProfile.query.all()
    return render_template('profiles.html', users=users)

@app.route('/profile/<userid>')
def get_user(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    return render_template('user.html',user=user)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

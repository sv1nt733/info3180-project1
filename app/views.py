"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, send_from_directory,flash
from app.models import Properties
from app.forms import createPropertyForm
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Dillon Waugh")

@app.route('/properties/create', methods = ['POST', 'GET'])
def addProperty():
    form = createPropertyForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        propertyType = form.propertyType.data
        description = form.description.data

        photo = form.photo.data
        photo_filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

        newProp= Properties(title, description, bedrooms, bathrooms, location, price, propertyType, photo=photo_filename)
        db.session.add(newProp)
        db.session.commit()

        flash('Property has been added', 'success')
        return redirect(url_for('allProperties'))

    return render_template('newProperty.html', form=form)

@app.route('/properties/')
def allProperties():
    """For displaying a list of all properties in the database."""
    properties = Properties.query.all()
    return render_template('allProperties.html', properties = properties)

@app.route('/property/<propertyid>')
def singleProperty(propertyid):
    singleProp= Properties.query.filter_by(id=propertyid).first()
    return render_template('singleProperty.html', singleProp=singleProp)

@app.route('/uploads/<filename>')
def fetchImage(filename):
    rootdirectory = os.getcwd()
    return  send_from_directory(os.path.join(rootdirectory,app.config['UPLOAD_FOLDER']),filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

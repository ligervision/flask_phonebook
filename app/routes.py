from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
from app.models import User

@app.route("/")
def index():
    print('hello')
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():

        # Get the data from the form fields
        last_name = form.last_name.data
        first_name = form.first_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
        zip_code = form.zip_code.data

        # Query the User table for any users with phone_number from form
        user_check = User.query.filter((User.phone_number == phone_number)).all()
        if user_check:
            flash('A user with that phone number already exists. Please try again.', 'danger')
            return redirect(url_for('signup'))

        # Add the user to the database
        new_user = User(last_name=last_name, first_name=first_name, phone_number=phone_number, address=address, city=city, state=state, zip_code=zip_code)

        # Show message of success/failure
        flash(f'{new_user.first_name} {new_user.last_name} has successfully signed up!', 'success')

        # redirect back to the homepage
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)
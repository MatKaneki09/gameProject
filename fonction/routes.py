from flask import Blueprint, render_template, request, redirect, url_for, flash
from fonction.models import db, User
from fonction.forms import SignupForm

routes = Blueprint('routes', __name__)

# Page d'accueil
@routes.route('/')
def presentation():
    return render_template('index.html')

# Page d'inscription
@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        pseudo = form.pseudo.data
        password = form.password.data

        # Vérification si le pseudo existe déjà
        existing_user = User.query.filter_by(pseudo=pseudo).first()
        if existing_user:
            flash('Ce pseudo est déjà pris.', 'danger')
            return redirect(url_for('routes.signup'))

        # Ajouter l'utilisateur dans la base de données
        new_user = User(pseudo=pseudo, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Inscription réussie !', 'success')
        return redirect(url_for('routes.presentation'))

    return render_template('signin.html', form=form)

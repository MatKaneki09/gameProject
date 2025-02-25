from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .app import app, db
from .models import User

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        password = request.form['password']

        # Vérification que le pseudo n'existe pas déjà
        user = User.query.filter_by(pseudo=pseudo).first()
        if user:
            flash("Ce pseudo est déjà utilisé.", "error")
            return redirect(url_for('signup'))

        # Vérification du mot de passe
        if len(password) <= 10:
            flash("Le mot de passe doit contenir plus de 10 caractères.", "error")
            return redirect(url_for('signup'))
        if not any(char.isdigit() for char in password):
            flash("Le mot de passe doit contenir au moins un chiffre.", "error")
            return redirect(url_for('signup'))
        if not any(char.isupper() for char in password):
            flash("Le mot de passe doit contenir une majuscule.", "error")
            return redirect(url_for('signup'))
        if not any(char in "!@#$%^&*()" for char in password):
            flash("Le mot de passe doit contenir un caractère spécial.", "error")
            return redirect(url_for('signup'))

        # Créer un nouvel utilisateur
        hashed_password = generate_password_hash(password)
        new_user = User(pseudo=pseudo, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Inscription réussie, vous pouvez maintenant vous connecter.", "success")
        return redirect(url_for('signin'))

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        password = request.form['password']

        # Vérification des identifiants
        user = User.query.filter_by(pseudo=pseudo).first()
        if user and check_password_hash(user.password, password):
            flash("Connexion réussie.", "success")
            return redirect(url_for('dashboard'))  # Redirection vers le dashboard après connexion
        else:
            flash("Identifiants incorrects.", "error")
            return redirect(url_for('signin'))

    return render_template('signin.html')

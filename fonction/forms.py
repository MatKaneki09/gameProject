from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

class SignupForm(FlaskForm):
    pseudo = StringField('Pseudo', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Mot de passe', validators=[
        DataRequired(), 
        Length(min=10), 
        Regexp('^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])', message="Le mot de passe doit contenir une majuscule, un chiffre, un caractère spécial et être plus long que 10 caractères.")
    ])

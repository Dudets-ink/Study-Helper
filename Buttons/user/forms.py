from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    
class RegisterForm(FlaskForm):
    user_len_warn = "Username can't be longer than 25 characters"
    pass_len_warn = "Passwords must be similiar"
    
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                                Length(max=25,message=user_len_warn)
                                ])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password',
                              validators=[DataRequired(),
                                    EqualTo('password',
                                            message=pass_len_warn)
                                    ])
    
    
    
    
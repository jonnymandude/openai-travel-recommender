# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration


class QuestionForm(FlaskForm):
    location = StringField('Location',
                         id='location',
                         validators=[DataRequired()])
    StartDate = PasswordField('StartDate',
                             id='StartDate',
                             validators=[DataRequired()])

    EndDate = PasswordField('EndDate',
                             id='EndDate',
                             validators=[DataRequired()])

    Interests = PasswordField('Interests',
                             id='Interests',
                             validators=[DataRequired()])
                    
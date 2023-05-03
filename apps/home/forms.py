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
    StartDate = StringField('StartDate',
                             id='StartDate',
                             validators=[DataRequired()])

    EndDate = StringField('EndDate',
                             id='EndDate',
                             validators=[DataRequired()])

    Interests = StringField('Interests',
                             id='Interests',
                             validators=[DataRequired()])
                    
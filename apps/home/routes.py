# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps.lib.ai import OpenAIClient
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps.home.forms import QuestionForm


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route('/travel', methods=['GET', 'POST'])
@login_required
def travel():

    question_form = QuestionForm(request.form)
    if 'location' in request.form:
        recommendation = OpenAIClient().vacation_recommendation(
            request.form['location'],
            request.form['StartDate'],
            request.form['EndDate'],
            request.form['Interests']
        )

        print(recommendation)

        return render_template('home/recommendation.html',
                               msg=recommendation["content"])



    return render_template('home/travel.html', segment='travel', form = question_form)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

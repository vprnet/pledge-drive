from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL


@app.route('/')
def index():
    page_title = 'Give Us Your Best Pitch'
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    social = {
        'title': "Give Us Your Best Pitch!",
        'subtitle': "",
        'img': "http://www.vpr.net/apps/dorothys-list/static/img/vpr-logo.png",
        'description': "Give us your best pitch!",
        'twitter_text': "Give us your best pitch!",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        social=social)

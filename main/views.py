from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL


@app.route('/')
def index():
    page_title = 'You Do The Pledge Drive'
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    social = {
        'title': "",
        'subtitle': "",
        'img': "https://s3.amazonaws.com/www.vpr.net/sandbox/app/static/img/vpr-glue.gif",
        'description': "I'm recording a pledge drive pitch for VPR!",
        'twitter_text': "I'm recording a pledge drive pitch for VPR!",
        'creator': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        social=social)

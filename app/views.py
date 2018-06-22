from flask import render_template
from app import app
from .request import get_sources,get_article


@app.route('/')
def index():
    """
    Function that returns the index page and all its data
    """
    sport_news = get_sources('sports')
    tech_news = get_sources('technology')
    title = 'News Highlights by Ephantus'
    return render_template('index.html', title=title, sports=sport_news, technology=tech_news)


@app.route('/source/<id>')
def articles(id):
    """
    View articles
    """
    article = get_article(id)
    print(article)
    title = f'Ephy News ~ {id}'
    return render_template('news.html', title=title, article=article)

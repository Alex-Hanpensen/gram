from app import app
from flask import render_template, request
from utils import *
import logging


@app.route('/')
def main():
    get_post = get_posts_all()
    return render_template('index.html', get_post=get_post)


@app.route('/post.html/<int:post_id>')
def get_post_id(post_id):
    comments = get_comments_by_post_id(post_id)
    post = get_post_by_pk(post_id)
    return render_template('post.html', post=post, count=len(comments), comments=comments)


@app.route('/search', methods=['POST', 'GET'])
def get_search():
    if request.method == 'POST':
        search = search_for_posts(request.form['search'])
        return render_template('search.html', search=search, count=len(search))
    return 'posts not found'


@app.route('/user-feed.html/<user_name>')
def get_user(user_name):
    user = get_posts_by_user(user_name)
    return render_template('user-feed.html', user=user)


@app.route('/api/posts')
def get_posts_api():
    get_posts = get_posts_all()
    logging.info('Request all posts  /api/posts')
    return json.dumps(get_posts, ensure_ascii=False)


@app.route('/api/posts/<int:post_id>')
def get_post_api(post_id):
    post = get_post_by_pk(post_id)
    logging.info(f'Post Request  /api/posts/{post_id}')
    return json.dumps(post, ensure_ascii=False)


@app.errorhandler(404)
def code_404(error):
    return render_template('code_404.html', code=404), 404


@app.errorhandler(500)
def code_404(error):
    return render_template('code_404.html', code=500), 500

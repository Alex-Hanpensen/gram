import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(path) -> FileNotFoundError | list[dict]:
    path = os.path.join(BASE_DIR, fr"app\static\data{path}")
    try:
        return json.load(open(path, 'r', encoding="utf8"))
    except FileNotFoundError:
        raise FileNotFoundError('file is not found')


def get_posts_all() -> list[dict]:
    return read(r'\posts.json')


def get_posts_by_user(user_name: str) -> list[dict]:
    data: list[dict] = read(r'\posts.json')
    return list(filter(lambda x: x['poster_name'] == user_name, data))


def get_comments_by_post_id(post_id: int) -> ValueError | list:
    data: list[dict] = read(r'\comments.json')
    comments = list(filter(lambda x: x['post_id'] == post_id, data))
    if comments:
        return comments
    raise ValueError('the post is missing')


def search_for_posts(query: str) -> list[dict]:
    data: list[dict] = read(r'\posts.json')
    return [post for post in data if query in post['content']]


def get_post_by_pk(pk: int) -> list[dict]:
    data: list[dict] = read(r'\posts.json')
    return list(filter(lambda x: x['pk'] == pk, data))



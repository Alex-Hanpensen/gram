from utils import get_posts_by_user, get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts


def test_get_posts_all():
    assert len(get_posts_all()) != 0
    assert get_posts_by_user('leo') is not None
    assert get_comments_by_post_id(1) is not None
    assert get_post_by_pk(1) is not None
    assert search_for_posts('Ага, опять еда!') is not None

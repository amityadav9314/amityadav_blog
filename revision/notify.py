from datetime import datetime, timedelta

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

from sql_services import get_many_db_object


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_notes_to_revise, 'interval', minutes=1)
    scheduler.start()


def fetch_notes_to_revise():
    # Fetch last 3 days posts
    d0 = datetime.today().strftime("%Y-%m-%d")
    d3 = (datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d")

    fields = {
        'publication_date__range': [d3, d0]
    }
    posts_db_obj = get_many_db_object(
        module='posts.models',
        model_name='Posts',
        _select_related=None,
        _prefetch_related="authors, categories",
        **fields
    )

    msg = []
    for post in posts_db_obj:
        msg.append(post.get_absolute_url())
    users = [1205325625, 1284470210]
    for user in users:
        url = settings.TELEGRAM_URL.format(
            token=settings.TELEGRAM_TOKEN,
            messager=msg,
            user=user
        )
        requests.get(url)
    print("users notified")

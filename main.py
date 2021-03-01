import requests
import logging
import config.log as log


def get_rss() -> str:
    req = requests.get("https://lenta.ru/rss/news")
    content = req.content.decode("utf-8")
    logging.info(content)
    req.close()
    return content


log.conf()
get_rss()

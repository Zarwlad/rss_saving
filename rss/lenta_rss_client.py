import requests
import logging
import xml.etree.ElementTree as ET

from dataclasses import dataclass
import typing


@dataclass
class LentaDto:
    author: str
    news_link: str
    title: str
    descr: str
    created_at: str
    category: str


def get_rss() -> str:
    req = requests.get("https://lenta.ru/rss/news")
    content = req.content.decode("utf-8")
    logging.debug(content)
    req.close()
    return content


def get_lenta_dto(content: str) -> tuple[LentaDto]:
    news_list = []
    root = ET.fromstring(content)
    for child in root:
        for ch in child:
            if "item" == ch.tag:
                news = LentaDto(str(ch[1].text),
                                str(ch[0].text),
                                str(ch[2].text),
                                str(ch[4].text).strip(),
                                str(ch[5].text),
                                str(ch[7].text))
                logging.info(news)
                news_list.append(news)

    return tuple(news_list)

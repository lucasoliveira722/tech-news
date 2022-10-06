from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    tuples_list = []
    title_search = {"title": {"$regex": title, '$options': 'i'}}
    filtered_news_list = search_news(title_search)
    for news in filtered_news_list:
        tuples_list.append((news["title"], news["url"]))
    return tuples_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    dated_list = []
    formatted_date = try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    date_search = {"timestamp": formatted_date}
    filtered_news_list = search_news(date_search)
    for news in filtered_news_list:
        dated_list.append


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

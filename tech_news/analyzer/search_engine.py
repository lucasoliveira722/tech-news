from tech_news.database import search_news


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


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

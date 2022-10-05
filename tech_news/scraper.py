import time
import requests
from parsel import Selector
from tech_news.database import create_news
# Requisito 1


def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
# html_content é igual ao retorno da fetch, o q vai no Selector
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news_links = selector.css('.entry-title a::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_button = selector.css('.nav-links .next::attr(href)').get()
    return next_page_button


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

# foi
    url = selector.css(
        "link[rel=canonical]::attr(href)"
    ).get()

# foi
    title = (selector.css(
        ".entry-title::text"
    ).get()).strip()

# foi
    timestamp = selector.css(
        ".entry-header-inner .post-meta .meta-date::text"
    ).get()

# foi
    writer = selector.css(
        ".entry-header-inner .post-meta .meta-author .author a::text"
    ).get()

# foi
    # https://www.geeksforgeeks.org/python-extract-numbers-from-string/
    comments_count = selector.css(
        ".post-comments h5::text"
    ).getall()
    comments_number = len(comments_count)

    # summary = selector.css(
    #     ".entry-content-wrap .entry-content p::text"
    # ).getall()[0]
    # summary_text = summary.strip()

# seleciona todos os textos:
# https://parsel.readthedocs.io/en/latest/usage.html#extensions-to-css-selectors
# https://devhints.io/xpath
    summary = "".join(selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()).strip()

# foi
    tags = selector.css(
        ".entry-content-wrap .post-tags ul li a::text"
    ).getall()

# foi
    category = selector.css(
        ".label::text"
    ).get()

    noticia = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_number,
        "summary": summary,
        "tags": tags,
        "category": category
    }

    return noticia


# Requisito 5
def get_tech_news(amount):
    base_url = "https://blog.betrybe.com"
    news_list = []

    while (len(news_list) < amount):
        url_info = fetch(base_url)
        news_scraped_list = scrape_novidades(url_info)
        for link in news_scraped_list:

            each_new = scrape_noticia(fetch(link))
            news_list.append(each_new)
            if (len(news_list) == amount):
                create_news(news_list)
                return news_list

        base_url = scrape_next_page_link(url_info)

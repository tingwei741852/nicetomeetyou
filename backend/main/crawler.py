import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import News
from .serializers import NewsSerializer
from django_redis import get_redis_connection
import json

def fetch_news():
    index_url = 'https://tw-nba.udn.com/nba/index'
    response = requests.get(index_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    slide = soup.find('ul', class_='splide__list')
    if slide:
        news_items = []
        news_href_list = []
        existing_news_hrefs = News.objects.values_list('news_href', flat=True)
        # print(existing_news_hrefs)
        
        for news in slide.find_all('li'):
            try:
                a_tag = news.find('a')
                img = news.find('img')
                news_href = a_tag['href']
                img_href = img['src']
                title = a_tag['title']
                news_href_list.append(news_href)
                if news_href in existing_news_hrefs:
                    News.objects.filter(news_href=news_href).update(display=True)
                    continue
                
                content_response = requests.get(news_href)
                content_soup = BeautifulSoup(content_response.text, 'html.parser')
                content = content_soup.find('div', id='story_body_content')

                if content:
                    for ul in content.find_all('ul'):
                        ul.decompose()
                    for element in content.find_all(class_='set_font_size'):
                        element.decompose()

                    html_content = str(content)
                    time = content.find('div', class_='shareBar__info--author').find('span')
                    date_time_format = "%Y-%m-%d %H:%M"
                    published_at = datetime.strptime(time.text, date_time_format)

                    news_items.append(News(
                        title=title,
                        news_href=news_href,
                        img_href=img_href,
                        content=html_content,
                        published_at=published_at,
                        display=True
                    ))
                else:
                    print(f"No content found for news: {news_href}")

            except Exception as e:
                print(f"Error processing news: {e}")

        created_count = 0
        News.objects.exclude(news_href__in=news_href_list).update(display=False)
        if news_items:
            created_objs = News.objects.bulk_create(news_items)
            created_count = len(created_objs)
            cacheCon = get_redis_connection("default")
            display_news = News.objects.filter(display=True)
            focusNews = NewsSerializer(display_news, many=True).data
            cacheCon.set('focusNews', json.dumps(focusNews))
        
        
        return created_count
    else:
        print("沒有找到slide")

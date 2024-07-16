import requests
import pandas as pd
import csv

api_link = "https://newsapi.org/v2/everything?"
api_key = "80423fcb354f45ea8fb17e14b61fc04a"

def get_news(api_link, api_key):

    topic = input("Tópico: ")
    from_date = input("A partir da data (formato YYYY-MM-DD): ")
    sort_by = "popularity"

    articles = get_news(api_link, topic, from_date, sort_by, api_key)
    organize_date_to_write(articles)


    url = f"{api_link}q={topic}&from={from_date}&sortBy={sort_by}&apiKey={api_key}"
    response = requests.get(url) 

    if response.status_code == 200:
        content = response.json()
        article = content.get('articles', [])

        return article
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return[]

def write_news_to_csv(articles):
    print("No articles to write.")
    return []

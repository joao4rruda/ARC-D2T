def organize_data_to_write(articles):
    if not articles:
        print("No articles to write.")
        return
    
    data =[(article['author'],
            article['title'],
            article['description'],
            article['content'],
            article['url'],
            article['urlToImage'],
            article['publishedAt']) for article in articles]
    
    for author, title, description, content, url, urlToImage, publishedAt, in data:
        put_int_form(author, title, description, content, url, urlToImage, publishedAt)
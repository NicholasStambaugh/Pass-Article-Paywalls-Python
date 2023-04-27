# A more pythonic version
from newspaper import Article
import nltk

# Define the URLs of the newsletter articles to summarize
newsletter_urls = [
    'https://example.com/article1',
    'https://example.com/article2',
    'https://example.com/article3'
]

# Download and summarize each article
for url in newsletter_urls:
    with Article(url) as article:
        article.download()
        article.parse()
        article.nlp()
        
        # Print the title, URL, and summary of the article
        print(f"Title: {article.title}")
        print(f"URL: {article.url}")
        print(f"Summary: {article.summary}\n")

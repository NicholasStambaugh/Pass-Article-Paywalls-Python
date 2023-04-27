# Newspaper and NLTK Newsletter Article Summarizer
This Python script uses the newspaper and nltk libraries to download and summarize newsletter articles.

### Requirements
Python 3.6 or higher

newspaper library

nltk library

### Installation
To install newspaper and nltk, you can use pip:

```
pip install newspaper3k
pip install nltk
```

You will also need to download the punkt tokenizer for nltk. You can do this by running the following command in Python:

```
import nltk
nltk.download('punkt')
```

## Usage
To use this script, replace 'place_article_url_here' with the URL of the newsletter article you want to summarize. You can add as many articles as you want to the newsletter_list list.

```
newsletter_list = [
    'https://example.com/article1',
    'https://example.com/article2',
    'https://example.com/article3'
]

for article in newsletter_list:
    newsletter = Article(url="%s" % article)
    
    newsletter.download()
    newsletter.parse()
    newsletter.nlp()
    
    print(newsletter.title)
    print(newsletter.url)
    print(newsletter.summary)
    print(newsletter.set_summary)
    print(newsletter.text)
```

When you run the script, it will download the article, parse it, and use nltk to generate a summary of the article. It will then print out the title, URL, summary, set_summary, and text of the article.


# Pythonic.py

This is a pythonic version of the newsletter article summarizer script that uses the newspaper and nltk libraries. The script takes a list of newsletter article URLs, downloads and summarizes each article, and prints the title, URL, and summary of each article. 

It uses list comprehension to iterate over the URLs and the with statement to ensure proper resource management. The code is more concise and readable than the previous version, using descriptive variable names and f-strings for string formatting.

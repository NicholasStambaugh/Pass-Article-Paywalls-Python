from newspaper import Article
import nltk

 


newsletter_list = [
        

 

'place_article_url_here'

 

]

 

for article in newsletter_list:
    newsletter = Article(url="%s" % article)

 

    nltk.download('punkt')       #Apparently this is required in order to execute the nlp. Nlp is then requried to call summary function.

 


    newsletter.download()    #downdload and parse need to be called before nlp is called.
    newsletter.parse()
    newsletter.nlp()

 


    print(newsletter.title)
    print(newsletter.url)
    print(newsletter.summary)
    print(newsletter.set_summary)
    print(newsletter.text)

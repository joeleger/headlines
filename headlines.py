import feedparser
from flask import Flask, render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'hacker': 'https://hnrss.org/newest',
             'Rome': 'https://www.omnycontent.com/d/playlist/4b5f9d6d-9214-48cb-8455-a73200038129/a7c446d6-29da-43ba-bbe5-a7da00ecda4a/a65603a6-cf22-4150-91c1-a7da00ed5220/podcast.rss',
             'Rogan' :'http://podcasts.joerogan.net/feed'}



@app.route('/')
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles = feed['entries']
    return render_template("home.html", articles=articles)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

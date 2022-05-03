from flask import Flask, render_template 
from newsapi import NewsApiClient
from pip import main

app = Flask(__name__)

@app.route('/')
def home():


 newsapi =NewsApiClient(api_key='6cc037b2e9984d0b995fb8d87f06d897')

 top_headlines = newsapi.get_top_headlines(sources='bbc-news') 

 t_articles = top_headlines['articles'] 

 return render_template('index.html', all = all)


if __name__ == '__main__':
    app.run(debug=True)

import requests
from bs4 import BeautifulSoup
from loader import load_env
from joke import Joke


load_env()

class TwitterScraper(object):
    BASE_URL = 'https://twitter.com/'

    def __init__(self, user='baddadjokes'):
        self.user = user

    def scrape(self):
        for tweet in self._tweets():
            Joke(
                self._tweet_ref(tweet),
                self._tweet_content(tweet),
                self._tweet_url(tweet),
                self.user
            ).save()

    def _tweet_content(self, tweet):
        return tweet.find(
                'div', 'tweet'
            ).find(
                'div', 'content'
            ).find(
                'div', 'js-tweet-text-container'
            ).find('p').get_text()

    def _tweet_id(self, tweet):
        return tweet['data-item-id']

    def _tweet_url(self, tweet):
        return "{0}{1}/status/{2}".format(
            self.BASE_URL,
            self.user,
            self._tweet_id(tweet)
        )

    def _tweet_ref(self, tweet):
        return "{0} - {1}".format(
            self.user,
            self._tweet_id(tweet)
        )

    def _tweets(self):
        page = self._twitter_page().text
        soup = BeautifulSoup(page, 'html.parser')

        return soup.find_all('li', 'js-stream-item')

    def _twitter_page(self):
        return requests.get('{0}{1}'.format(
            self.BASE_URL,
            self.user
        ))

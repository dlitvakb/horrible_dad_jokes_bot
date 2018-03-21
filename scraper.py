import requests
from bs4 import BeautifulSoup
from models import Joke


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


class ICanHazDadJokeScraper(object):
    BASE_URL = 'https://icanhazdadjoke.com/'
    SOURCE = 'iCanHazDadJoke'

    def scrape(self):
        for joke in self._jokes():
            Joke(
                self._joke_ref(joke),
                self._joke_content(joke),
                self._joke_url(joke),
                self.SOURCE
            ).save()

    def _joke_ref(self, joke):
        return "{0} - {1}".format(self.BASE_URL, joke['id'])

    def _joke_content(self, joke):
        return joke['joke']

    def _joke_url(self, joke):
        return "{0}/j/{1}".format(self.BASE_URL, joke['id'])

    def _jokes(self):
        jokes = []
        next_page = 1

        while next_page is not None:
            results = requests.get(
                '{0}/search?page={1}'.format(self.BASE_URL, next_page),
                headers={'accept': 'application/json'}
            ).json()

            jokes += results['results']

            if results['next_page'] != next_page:
                next_page = results['next_page']
            else:
                next_page = None

        return jokes



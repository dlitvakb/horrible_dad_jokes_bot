from scraper import TwitterScraper, ICanHazDadJokeScraper

scrapers = [
    TwitterScraper('baddadjokes'),
    ICanHazDadJokeScraper()
]

if __name__ == '__main__':
    for scraper in scrapers:
        scraper.scrape()

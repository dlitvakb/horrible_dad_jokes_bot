from scraper import TwitterScraper

scrapers = [
    TwitterScraper('baddadjokes')
]

if __name__ == '__main__':
    for scraper in scrapers:
        scraper.scrape()

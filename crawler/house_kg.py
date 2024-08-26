import requests
from parsel import Selector
# from pprint import pprint


class HouseCrawler:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    def __init__(self):
        page = requests.get(url=HouseCrawler.MAIN_URL)
        self.page = page.text

    def get_links(self):
        html = Selector(text=self.page)
        links = html.css('div.listings-wrapper div.listing div.main-wrapper div.left-image a::attr(href)').getall()
        links = list(map(lambda link: HouseCrawler.BASE_URL + link, links))
        # pprint(links)
        return links


if __name__ == '__main__':
    crawler = HouseCrawler()
    crawler.get_links()

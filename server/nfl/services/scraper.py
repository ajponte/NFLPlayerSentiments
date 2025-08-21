"""Web Scraper Service Object and helper methods."""
from abc import ABC

# from playwright.sync_api import sync_playwright

import nfl.snscrape.snscrape.modules.twitter as sntwitter

from nfl.error import DownstreamApiException
from nfl.services.posts import XPostsIterator, PostsCollection


class Scraper(ABC):
    def __init__(
        self,
        max_results: int
    ):
        self._max_results = max_results

    def scrape(self, pattern: str) -> list:
        """Scrape a site for a pattern and return results."""
        pass


class XSnsScraper(Scraper):
    """Uses the `snscrape` package to scrape `X` based on a query."""
    def __init__(
        self,
        max_results: int
    ):
        super().__init__(max_results=max_results)

    # def scrape(self, query: str) -> list:
    #     try:
    #         import snscrape.modules.twitter as sntwitter
    #     except Exception as e:
    #         raise ValueError(f'Could not import snstwitter')
    #     """Scrape `X` based on the `query`."""
    #     scraped = []
    #     for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    #         if i >= self._max_results:
    #             break
    #         scraped.append([
    #             tweet.id,
    #             tweet.date,
    #             tweet.user.username,
    #             tweet.content.replace("\n", " "),
    #             tweet.likeCount,
    #             tweet.retweetCount
    #         ])
    #     return scraped
    def scrape(self, query: str) -> list:
        scraped = []
        try:
            import pdb; pdb.set_trace()
            tweets = sntwitter.TwitterSearchScraper(query).get_items()
            # posts_iter = XPostsIterator(collection=PostsCollection(tweets))
            # while posts_iter.has_more():
            #     scraped.append(next(posts_iter))
            # # print(vars(tweets))
        except Exception as e:
            msg = f'Error webscraping with snscrape. Error: {e}'
            raise DownstreamApiException(message=msg, cause=e) from e

        return scraped

# class XPlaywrightScrapper(Scraper):
#     """Uses `Playwright` to scrape `X` data based on a query."""
#     def __init__(self, max_results: int):
#         super().__init__(max_results=max_results)
#
#     def scrape(self, query: str) -> list:
#         _xhr_calls = []
#         # for testing
#         # url = "https://twitter.com/Scrapfly_dev/status/1664267318053179398"
#         url = f"https://twitter.com/search?q={query}"
#         def intercept_response(response):
#             """capture all background requests and save them"""
#             # we can extract details from background requests
#             if response.request.resource_type == "xhr":
#                 _xhr_calls.append(response)
#             return response
#
#         with sync_playwright() as pw:
#             browser = pw.chromium.launch(headless=True)
#             context = browser.new_context(viewport={"width": 1920, "height": 1080})
#             page = context.new_page()
#
#             # enable background request intercepting:
#             page.on("response", intercept_response)
#             # go to url and wait for the page to load
#             page.goto(url)
#             page.wait_for_selector("[data-testid='tweet']")
#
#             # find all tweet background requests:
#             tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
#             for xhr in tweet_calls:
#                 data = xhr.json()
#                 return [data['data']['tweetResult']['result']]
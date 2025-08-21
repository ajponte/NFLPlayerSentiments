"""Client wrapper for x.com."""
import tweepy
import csv
from typing import Any

from tweepy import Response

from nfl.error import DownstreamApiException
from nfl.services.scraper import XSnsScraper

DEFAULT_FIELDS = ["created_at", "author_id", "public_metrics"]

# For typing
JSON_RESPONSE = dict[str, Any]

DEFAULT_MAX_RESULTS = 20

def configure_x_api_client(config: dict[str, Any]) -> 'XApiClient':
    """Configure and return a new API client."""
    return XApiClient(
        bearer=config['X_DOT_COM_BEARER_TOKEN'],
        wait_on_limit=config['X_DOT_COM_WAIT_ON_RATE_LIMIT'],
        webscrape_backup=config['X_DOT_COM_WEBSCRAPE_BACKUP'],
        cache_csv_file=config['CACHE_FILE']
    )


class XApiClient:
    def __init__(
        self,
        bearer: str,
        wait_on_limit: bool,
        webscrape_backup: bool,
        cache_csv_file: str
    ):
        """Constructor."""
        self._webscrape_backup = webscrape_backup
        # Instantiate the client
        self._client = tweepy.Client(
            bearer_token=bearer,
            # Wait on rate limit
            wait_on_rate_limit=wait_on_limit
        )
        self._cache_csv = cache_csv_file

    def search_posts(
        self,
        query: str,
        max_results:int=DEFAULT_MAX_RESULTS
    ) -> Any:
        """
        Perform a search on publicly available posts, and persist to a file.

        :param query: The query which the X API understands.
        :param max_results: The max number of posts to search.
        """
        results = None
        try:
            results = self._search_recent_tweets(
                query=query,
                fields=DEFAULT_FIELDS,
                max_results=max_results
            )
        except Exception as e:
            message = f"Unknown exception while fetching tweets: {e}"
            if not self._webscrape_backup:
                raise DownstreamApiException(message=message, cause=e) from e
            results = (
                XSnsScraper(max_results=max_results).scrape(query)
            )
            # results = (
            #     XPlaywrightScrapper(max_results=max_results).scrape(query)
            # )
        finally:
            # Save any results to csv.
            results = results or []
            _save_to_csv(results, filename=self._cache_csv)
        return results

    def _search_recent_tweets(
        self,
        query: str,
        fields: list[str],
        max_results: int
    ):
        """
        Perform the request.

        :param query: Query to search.
        :param fields: Posts metadata fields to group by.
        :param max_results: Max posts to fetch.
        """
        try:
            x_response = self._client.search_recent_tweets(
                query=query, tweet_fields=fields, max_results=max_results)
            return self._format_posts_result(posts=x_response, results=[])
        except Exception as e:
            message = f"Unknown exception while fetching tweets: {e}"
            raise DownstreamApiException(message=message, cause=e) from e

    def _format_posts_result(
        self,
        posts: Response,
        results: list[Any]
    ) -> list[Any]:
        """
        Formats the posts in the API response and append to the running list/

        :param posts: Results from the API call.
        :param results: The running list of results.
        :return: The list of results after appended.
        :raise: ValueError - If the list is not initialized.
        """
        if not results:
            raise ValueError('The list of results was not initialized.')

        for t in posts.data:
            metrics = t.public_metrics
            results.append([
                t.id,
                t.created_at,
                t.author_id,
                t.text.replace("\n", " "),
                metrics["like_count"],
                metrics["retweet_count"]
            ])
        return results

def _save_to_csv(tweets: list, filename: str) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "author_id", "text", "like_count", "retweet_count"])
        for t in tweets:
            writer.writerow(t)
    print(f"Saved {len(tweets)} tweets to {filename}")

# def _scrape_tweets(query: str, max_results: int):
#     """Fallback scraper using snscrape if API rate limited."""
#     import snscrape.modules.twitter as sntwitter
#     print("Falling back to scraping...")
#     scraped = []
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
#         if i >= max_results:
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

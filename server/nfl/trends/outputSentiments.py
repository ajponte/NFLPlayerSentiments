"""
Outputs the sentiments of the QUERY
@author Alan Ponte
"""

from CalculateSentiments import SentinmentCalculator
from getData import Twitter
from getData.utils import read_json_to_file
from getSentiments import load_sentiments
from pprint import pprint
import sys


def parse_text_file(json_file):
    """Returns a Parsed text JSON_FILE of Json strings."""
    infile = open(json_file)
    lines = []
    try:
        lines = infile.readlines()
    except:
        print("Error parsing JSON file.")
        sys.exit(1)

    pprint((lines))
    infile.close()
    return lines


def get_sentiments(query):
    """Finds and returns the Sentiments of Twitter strings
    based on the query."""

    json_file = "jsonOutput/" + query + ".json"
    text_file = "textOutput/" + query + ".txt"
    Twitter.search_for_query(query, 100, json_file)
    read_json_to_file(json_file, text_file)
    tweets = parse_text_file(text_file)
    sentiments = load_sentiments()
    se = SentinmentCalculator(tweets, sentiments)
    return se.analyze_tweet_sentiments()


def create_sentiment_report(query):
    """Creates a sentiment report based on the QUERY."""
    sentiments = get_sentiments(query)
    print(
        "Based on the query, {q} has a sentiment value of {sents}".format(
            q=query, sents=sentiments
        )
    )

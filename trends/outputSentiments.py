'''
Outputs the sentiments of the WORD
@author Alan Ponte
'''
from CalculateSentiments import SentinmentCalculator
from getData import Twitter
from getData.utils import read_json_to_file
from getSentiments import load_sentiments
from pprint import pprint
from ucb import *

def parse_text_file(file):
    """ Returns a Parsed a text file of Json strings."""
    infile = open(file)
    lines = []
    lines = infile.readlines()
    #while infile is not None:
        #lines.append(infile.readline())
    #lines = infile.readlines()
    pprint((lines))
    infile.close()
    return lines

def get_sentiments(query):
    """ Finds and retuns the Sentiments of Twitter strings
        based on the query."""
    
    json_file = "jsonOutput/" + query + ".json"
    text_file = "textOutput/" + query + ".txt"
    Twitter.search_for_query(query, 100, json_file)
    read_json_to_file(json_file, text_file) 
    tweets = parse_text_file(text_file)
    sentiments = load_sentiments()
    se = SentinmentCalculator(tweets, sentiments) 
    return se.analyze_tweet_sentiments()
         
def main():
    query = "Carlos Rodgers"
    pprint(get_sentiments(query))
    interact()

    
if __name__ == "__main__":
    main()

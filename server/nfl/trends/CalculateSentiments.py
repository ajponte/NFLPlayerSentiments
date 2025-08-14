''' Calculates the sentiments from Tweets. 
    @author: Alan Ponte
'''

from __future__ import print_function
from getSentiments import load_sentiments
import string

class SentinmentCalculator:
    """ Given a list of TWEETS and dictionary
        of SENTIMENTS, performs operations to find
        the average sentiment, etc.
    """
    def __init__(self, tweets, sentiments):
        self.tweets = tweets
        self.sentiments = sentiments
        
    def analyze_tweet_sentiments(self):
        """ Analyzes the sentiments of the TWEETS.
        """
        total_sentiments = 0.0
        for tweet in self.tweets:
            total_sentiments += self.average_sentiment(tweet)
        return total_sentiments/len(self.tweets)
            
            
    def average_sentiment(self, tweet):
        """ Returns the average sentiment of the TWEET 
            based on the sentiment dictionary.
        """
        total = 0.0
        count = 0
        average = 0.0
        words = self.extract_words(tweet)
        for word in words:
            word = word.replace(" ' ", '')
            try:
                curr_sentiment = self.sentiments[word]
                print("current sentiment of " + word + " : " + str(curr_sentiment))
            except KeyError:
                print(word + " not found in sentiments")
                curr_sentiment = 0.0
            total += curr_sentiment
            count += 1
        print("Total : " + str(total))
        print("Count : " + str(count))
        try:
            average = total/count
        except:
            print("Divide by zero error!")
        print("AVERAGE: " + str(average))
        return average
    
    def extract_words(self, tweet):
        """ Returns a list of extracted words from the TWEET. """
        numbers = ['1','2','3','4','5','6','7','8','9']
        for i in string.punctuation :
            tweet = tweet.replace(i, ' ')   #first, extract all punctuation
        for i in numbers:
            tweet = tweet.replace(i, ' ')   #then extract any integer strings
        return tweet.split()
    
    @property
    def sentiments(self):
        return self.sentiments
    
    @property
    def tweets(self):
        return self.tweets


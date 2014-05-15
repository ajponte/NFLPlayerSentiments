from CalculateSentiments import *
from getSentiments import *

def main():
    sentiments = load_sentiments()
    tweets = ["Quinton Patton is about the only person in this world who would've liked the May draft to take place last season.",
              "Yeah, tell me about it. But we've got it worse. --Signed, Rueben Randle and Quinton Patton Dynasty Owners. :("]
    se = SentinmentCalculator(tweets, sentiments)
    se.analyze_tweet_sentiments()
    
if __name__ == "__main__":
    main()

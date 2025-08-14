''' Gathers the sentiments from the sentiments dictionary
    @author Alan Ponte
'''
from __future__ import print_function
import sys
from pprint import pprint

def open_sentiments_file(file):
    """ Opens the sentiments FILE. """
    sentiments_dict = {}
    with open(file) as data_file:
        pass
        
def load_sentiments(file_name = "sentiments.csv"):
    """Read the sentiment file and return a dictionary containing the sentiment
    score of each word, a value from -1 to +1.
    """
    sentiments = {}
    for line in open(file_name):
        word, score = line.split(',')
        sentiments[word] = float(score.strip())
    return sentiments

word_sentiments = load_sentiments()

def main():
    sentiments = load_sentiments()
    pprint(sentiments['higher'])

if __name__ == "__main__":
    main()
    
        

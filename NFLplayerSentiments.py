'''Main Entry Point.
   Usage:  python NFLplayerSentiments.py 'QUERY' 
   (with quotes).
   @author Alan Ponte
'''

from __future__ import print_function
import sys
from server.nfl.trends import get_sentiments
from server.nfl.trends import create_sentiment_report
import xml.etree.ElementTree as ET

def createReport(query):
    """ Creates a sentiment report based on the QUERY."""
    sentiments = get_sentiments(query)
    print("Based on the query, %s has an average sentiment value of %d", query, sentiments)
    
def usage():
    """ Sends a usage message to the user. """
    print("Usage:\n python NFLplayerSentiments.py 'QUERY' (remember to include the quotes).")
    
def correct_player_name(name):
    """Returns True iff NAME is a name of a player in the XML database."""
    tree = ET.parse('players.xml')
    root = tree.getroot()
    for rt in root:
        if rt.attrib['name'] is name:
            return True
    return False

def main():
    #TO DO: Check in XML DB to see if player exists.
    
    try:
        query = sys.argv[1]
    except IndexError:
        usage()
        sys.exit(1)
    create_sentiment_report(query)
    
if __name__ == "__main__":
    main()

''' Functions for Traversing Twitter.
    @author Alan Ponte
'''
import sys
import os
import json
import twitter
from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

APP_NAME = 'GetDataByName'
CONSUMER_KEY = 's2zQh2LtwETQ65ojvG0U48LkV'
CONSUMER_SECRET = 'BUUaIZSMCnSGy3IMyKEIdUenFZ8D7E0UFeNftb1DMTORdkwhjB'

def search(t, q=None, max_batches=5, count=80):
    """ Searches Twitter for the query Q in batches of MAC_BATCHES. """
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = t.search.tweets(q=q, count=count)

    statuses = search_results['statuses']

    # Iterate through more batches of results by following the cursor
    for _ in range(max_batches):
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e: # No more results when next_results doesn't exist
            break
            # Create a dictionary from next_results, which has the following form:
            # ?max_id=313519052523986943&q=%23MentionSomeoneImportantForYou&include_entities=1
            kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
            search_results = twitter_api.search.tweets(**kwargs)
            print("found satus : ", search_results['statuses'])
            statuses += search_results['statuses']

    return statuses

def oauth_login(app_name=APP_NAME,
                consumer_key=CONSUMER_KEY, 
                consumer_secret=CONSUMER_SECRET, 
                token_file='out/twitter.oauth'):

    try:
        (access_token, access_token_secret) = read_token_file(token_file)
    except IOError, e:
        (access_token, access_token_secret) = oauth_dance(app_name, consumer_key,
                consumer_secret)

        if not os.path.isdir('out'):
            os.mkdir('out')

        write_token_file(token_file, access_token, access_token_secret)

        print >> sys.stderr, "OAuth Success. Token file stored to", token_file

    return twitter.Twitter(auth=server.trends.getData.twitter.oauth.OAuth(access_token, access_token_secret,
                                                                          consumer_key, consumer_secret))
    
def search_for_query(query, count, file_name):
    """ Searches for the specified QUERY, outputting the max COUNT
        to the FILE_NAME."""
    print("Searching twitter for " + query + "...")
    twitter = oauth_login(app_name = APP_NAME, consumer_key = CONSUMER_KEY,
                          consumer_secret = CONSUMER_SECRET, token_file = 'out/twitter.oauth')
    statuses = search(twitter, q = query)
    outfile = open(file_name, 'w')
    outfile.write(json.dumps(statuses, indent = 1))
    outfile.close()
    print("Done Searching!")
   
        

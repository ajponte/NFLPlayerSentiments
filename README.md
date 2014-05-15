NFLPlayerSentiments
===================

Creates a report of the Twitter "sentiments" of NFL Players, and teams as a whole

Synopis:
--------------
Ever wondered how favorable your NFL players are among Twitter?


USAGE:
==================
python NFLplayerSentiments.py 'QUERY' 
Where QUERY is the name of a player (remember the quotes)

OUTPUT:
================
For example, to find the Twitter sentiment of Aldon Smith, type
python NFLplayerSentiments.py 'Aldon Smith'

> python NFLplayerSentiments.py 'Jim Harbaugh'
>> "Based on the query, Jim Harbaugh has a sentiment value of .00956001"

+ The number returned is the average sentiment of the person on Twitter.
+ Let s be the sentiment value.
+ Then s is an integer such that -1 <= s <= 1

How it works
------------
+ The most common words in the english dictionary have been assigned an 
arbritary "sentiment" value.

- That is, there is an surjective function f, such that f(word) |--> sentiment

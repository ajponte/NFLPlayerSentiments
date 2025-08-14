''' Utility functions for getting Twitter Data
    @author Alan Ponte
'''
import json
from pprint import pprint

def read_json_to_file(in_file, out_file):
    """ Reads json data from the FILE and outputs
        to a text file.
    """
    strings = []
    with open(in_file) as data_file:
        data = json.load(data_file)
    jsonText = open(out_file, 'w')
    for text in data:
        try:
            str(text[""u'text'""])
            strings.append(str(text[""u'text'""]))
        except UnicodeEncodeError:
            pass
    
    for txt in strings:
        jsonText.write(txt + "\n")
    jsonText.close()
    print("Done writing to text file")
    

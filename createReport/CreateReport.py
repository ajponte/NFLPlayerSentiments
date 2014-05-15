'''
Creates a report for each entry in INFILE

Created on May 12, 2014

@author: Alan Ponte
'''
from __future__ import print_function
import sys
import csv

def main():
    infile = sys.argv[1]
    infile = None
    try:
        input_file = open(infile)
    except:
        print("Error opening INFILE")
        sys.exit(1)
        

    
if __name__ == "__main__":
    main()

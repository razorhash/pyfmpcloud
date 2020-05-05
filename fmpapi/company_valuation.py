from urllib.request import urlopen
import json
import pandas as pd
import configparser

cfg = configparser.ConfigParser()


url_root =  "https://financialmodelingprep.com/"

def rss_feed():
    """RSS Feed API from https://fmpcloud.io/documentation#rssFeed

    Returns:
        JSON -- Returns any filings of the day over the last week
    """        
    response = url_root + ''
    return 0
    


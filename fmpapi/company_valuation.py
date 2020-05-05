from urllib.request import urlopen
import pandas as pd
#import error

import configparser
cfg = configparser.ConfigParser()
cfg.read('../config.ini')
apikey = cfg['API']['api_key']
urlroot = cfg['API']['url_root']

def rss_feed():
    """RSS Feed API from https://fmpcloud.io/documentation#rssFeed

    Returns:
        JSON -- Returns any filings of the day over the last week
    """        
    localurl = "rss_feed?apikey="
    url = urlroot + localurl + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def balance_sheet(ticker, period = 'annual', bstype = 'full'):
    """Balance sheet API from https://fmpcloud.io/documentation#balanceSheet
    
    Input:
        ticker : ticker for which we need the balance sheet values
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
        bstype : 'full', 'growth', 'short', 'growth-short'. Defines input sheet type. Defaults to full. 
    Returns:
        Balance sheet info for selected tickers 
    """  
    
    typeurl = ''
    try:
        if bstype == 'full':
            typeurl = 'balance-sheet-statement/'
        elif bstype == 'growth':
            typeurl = 'balance-sheet-statement-growth/'
        elif bstype == 'short':
            typeurl = 'balance-sheet-statement-shorten/'
        elif bstype == 'growth-short':
            typeurl = 'balance-sheet-statement-growth-shorten/'
    except:
        print(error)
        print('Balance sheet type not correct')
        
    url = urlroot + typeurl + ticker + "?" + "datatype=csv&period=" + period + "&apikey=" + apikey
    data = pd.read_csv(url)
#    data = response.read().decode("utf-8").text
    return data
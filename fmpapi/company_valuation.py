from urllib.request import urlopen
import pandas as pd
import json

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

def balance_sheet(ticker, period = 'annual', ftype = 'full'):
    """Balance sheet API from https://fmpcloud.io/documentation#balanceSheet
    
    Input:
        ticker : ticker for which we need the balance sheet values
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
        ftype : 'full', 'growth', 'short', 'growth-short'. Defines input sheet type. Defaults to full. 
    Returns:
        Balance sheet info for selected ticker
    """  
    
    typeurl = ''
    try:
        if ftype == 'full':
            typeurl = 'balance-sheet-statement/'
        elif ftype == 'growth':
            typeurl = 'balance-sheet-statement-growth/'
        elif ftype == 'short':
            typeurl = 'balance-sheet-statement-shorten/'
        elif ftype == 'growth-short':
            typeurl = 'balance-sheet-statement-growth-shorten/'
    except:
        print('Balance sheet type not correct')
        
    url = urlroot + typeurl + ticker + "?" + "datatype=csv&period=" + period + "&apikey=" + apikey
    data = pd.read_csv(url)
    return data

def income_statement(ticker, period = 'annual', ftype = 'full'):
    """Income statement API from https://fmpcloud.io/documentation#incomeStatement
    
    Input:
        ticker : ticker for which we need the balance sheet values
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
        ftype : 'full', 'growth'. Defines input sheet type. Defaults to full. 
    Returns:
        Income statement info for selected ticker
    """
    typeurl = ''
    try:
        if ftype == 'full':
            typeurl = 'income-statement/'
        elif ftype == 'growth':
            typeurl = 'income-statement-growth/'
#        elif bstype == 'short':
#            typeurl = 'income-statement-shorten/'
#        elif bstype == 'growth-short':
#            typeurl = 'income-statement-growth-shorten/'
    except:
        print('Income statement type not correct')
        
    url = urlroot + typeurl + ticker + "?" + "period=" + period + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def cash_flow_statement(ticker, period = 'annual', ftype = 'full'):
    """Cash Flow Statement API from https://fmpcloud.io/documentation#cashFlowStatement
    
    Input:
        ticker : ticker for which we need the balance sheet values
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
        ftype : 'full', 'growth'. Defines input sheet type. Defaults to full. 
    Returns:
        Income statement info for selected ticker 
    """
    typeurl = ''
    try:
        if ftype == 'full':
            typeurl = 'cash-flow-statement/'
        elif ftype == 'growth':
            typeurl = 'cash-flow-statement-growth/'
#        elif bstype == 'short':
#            typeurl = 'income-statement-shorten/'
#        elif bstype == 'growth-short':
#            typeurl = 'income-statement-growth-shorten/'
    except:
        print('Cash Flow Statement type not correct')
        
    url = urlroot + typeurl + ticker + "?" + "period=" + period + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def financial_ratios(ticker, period = 'annual', ttm = False):
    """Financial Ratios API from https://fmpcloud.io/documentation#financialRatios
    
    Input:
        ticker : ticker for which we need the balance sheet values
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
        ttm: trailing twelve months financial ratios. Default is False
    Returns:
        Financial ratios info for selected ticker 
    """
    if ttm:
        typeurl = "ratios-ttm/"
    else:
        typeurl = "ratios/"
        
    url = urlroot + typeurl + ticker + "?" + "period=" + period + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)
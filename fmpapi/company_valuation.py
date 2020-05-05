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
        ticker : ticker for which we need the income statement
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
        ticker : ticker for which we need the cash flow statement
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
        ticker : ticker for which we need the financial ratios
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

def key_metrics(ticker, period = 'annual'):
    """Key Metrics API from https://fmpcloud.io/documentation#keyMetrics
    
    Input:
        ticker : ticker for which we need the key metrics
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
    Returns:
        Key metrics info for selected ticker 
    """
    typeurl = "key-metrics/"
    url = urlroot + typeurl + ticker + "?" + "period=" + period + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def enterprise_value(ticker, period = 'annual'):
    """Enterprise value API from https://fmpcloud.io/documentation#enterpriseValue
    
    Input:
        ticker : ticker for which we need the enterprise value
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
    Returns:
        Enterprise value info for selected ticker 
    """
    typeurl = "enterprise-values/"
    url = urlroot + typeurl + ticker + "?" + "period=" + period + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)
    
def financial_statements_growth(ticker, period = 'annual'):
    """Financial Statements Growth API from https://fmpcloud.io/documentation#financialStatementGrowth
    
    Input:
        ticker : ticker for which we need the financial growth
        period : 'annual', 'quarter'. Periodicity of requested balance sheet. Defaults to annual
    Returns:
        Financial Statements Growth info for selected ticker 
    """
    typeurl = "financial-growth/"
    url = urlroot + typeurl + ticker + "?" + "period=" + period + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def dcf(ticker, history = 'today'):
    """Discounted Cash Flow Valuation API from https://fmpcloud.io/documentation#dcf
    
    Input:
        ticker : ticker for which we need the dcf 
        history: 'today','daily', 'quarter', 'annual'. Periodicity of requested DCF valuations. Defaults to single value of today
    Returns:
        Discounted Cash Flow Valuation info for selected ticker 
    """
    try:
        if history == 'today':
            typeurl = 'discounted-cash-flow/'
            url = urlroot + typeurl + ticker + "?" + "apikey=" + apikey
        elif history == 'daily':
            typeurl = 'historical-daily-discounted-cash-flow/'
            url = urlroot + typeurl + ticker + "?" + "apikey=" + apikey
        elif history == 'annual':
            typeurl = 'historical-discounted-cash-flow-statement/'
            url = urlroot + typeurl + ticker + "?" + "apikey=" + apikey
        elif history == 'quarter':
            typeurl = 'historical-discounted-cash-flow-statement/'
            url = urlroot + typeurl + ticker + "?" + "period=" + history + "&apikey=" + apikey
    except:
        print('Discounted Cash Flow history requested not correct')
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def market_capitalization(ticker, history = 'today'):
    """Market Capitalization API from https://fmpcloud.io/documentation#marketCapitalization
    
    Input:
        ticker : ticker for which we need the Market Cap 
        history: 'today','daily'. Periodicity of requested Market Caps. Defaults to single value of today
    Returns:
        Market Cap info for selected ticker 
    """
    try:
        if history == 'today':
            typeurl = 'market-capitalization/'
        elif history == 'daily':
            typeurl = 'historical-market-capitalization/'
    except:
        print('Market Cap history requested not correct')
    url = urlroot + typeurl + ticker + "?" + "apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def rating(ticker, history = 'today'):
    """Rating API from https://fmpcloud.io/documentation#rating
    
    Input:
        ticker : ticker for which we need the rating info 
        history: 'today','daily'. Periodicity of requested ratings. Defaults to single value of today
    Returns:
        rating info for selected ticker 
    """
    try:
        if history == 'today':
            typeurl = 'rating/'
        elif history == 'daily':
            typeurl = 'historical-rating/'
    except:
        print('Rating history requested not correct')
    url = urlroot + typeurl + ticker + "?" + "apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)
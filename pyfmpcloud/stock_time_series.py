# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:29:40 2020

@author: Hashim Mazhar
"""
from urllib.request import urlopen
import pandas as pd
from pyfmpcloud import settings

def real_time_quote(ticker):
    """Real time quote API from https://fmpcloud.io/documentation#realtimeQuote
    
    Input:
        ticker : stock ticker of the company. eg: 'AAPL'
    Returns:
        Dataframe -- real-time quotes of the requested tickers
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    urlrtq = 'quote/'
    url = urlroot + urlrtq + ticker + "?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def ticker_search(match = None, limit = 100, exchange = 'NASDAQ'):
    """Ticker search API for partial matching of stocks over specified exchange. From https://fmpcloud.io/documentation#tickerSearch
    
    Input:
        match - string to match tickers. eg: 'AA' will return AAPL, AAON etc.
        limit - number of search results to return. Defaults to 100
        exchange - the exchange to perform the search on. Possible values 'NASDAQ', 'AEX', 'NYSE'. Will publish a complete list later
    Returns:
        Dataframe -- matching tickers, upto 'limit' number of values, found on the specified exchange
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    if match is not None:
        url = urlroot + 'search?query=' + match + '&limit=' + str(limit) + "&exchange=" + exchange + '&apikey=' + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)

def historical_stock_data():
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    return 0

def batch_request_eod_prices():
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    return 0

def available_markets_and_tickers():
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    return 0

def stock_market_performances():
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    return 0

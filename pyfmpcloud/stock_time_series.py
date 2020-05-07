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

def historical_stock_data(ticker, period = None, dailytype = None, last = None, start = None, end = None):
    """Historical stock data API for partial matching of stocks over specified exchange. From https://fmpcloud.io/documentation#historicalStockData
    
    Input:
        ticker - company for which you want the historical stock data
        period - tick periodicity - can be '1min', '5min', '15min', '30min', '1hour'. Defaults to '15min'. Do not use with daily type
        dailytype - can be 'line', 'change'. line chart info for daily stock or daily change and volume. Do not use with period.
        last - stock data for last x days. Only works with dailytype. Does not work with period 
        start - start date in the format yyyy-mm-dd. eg: '2018-01-01'
        end - end date in the format yyyy-mm-dd. eg: '2019-01-01'
    Returns:
        Dataframe -- historical stock data
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    if ((dailytype is not None) or (last is not None)) and (period is not None):
        raise Exception(" 'period' and 'dailytype' cannot be set on the same call. Please choose either, not both. 'last' can only be set with 'dailytype'")
    if dailytype is not None:
        urlhist = urlroot + 'historical-price-full/' + ticker + '?'
    elif period is not None:
        urlhist = urlroot + 'historical-chart/' + period + '/' + ticker + '?'
    else:
        raise Exception("'period' or 'dailytype' not set. Please set atleast one")
    if dailytype == 'daily':
        urlhist = urlhist + "serietype=line&"
    if last is not None:
        urlhist = urlhist + "timeseries=" + str(last) + "&"
    if (last is None) and (start is not None):
        urlhist = urlhist + "from=" + start + "?"
    if (last is None) and (end is not None):
        urlhist = urlhist + "to" + end + "?"
    url = urlhist+ "apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    data = pd.read_json(data)
    if dailytype is not None:
        datatick = data['symbol']
        data_mod = pd.DataFrame.from_records(data['historical'])
        data_mod['symbol'] = datatick
        data = data_mod
    data['date'] = pd.to_datetime(data['date'], format = '%Y-%m-%d %H:%M:%S')
    data = data.set_index('date')
    return data

def batch_request_eod_prices(tickers = None, date = None):
    """Daily candle stick data API for all available or specified tickers. From https://fmpcloud.io/documentation#batchEndOfTheDay
    
    Input:
        tickers - a list of strings only. Will not work as expected if 'AAPL' is sent. Please send ['AAPL'] for single stock and ['AAPL','FB','MSFT'] for a batch. Default value returns data for all available stocks. If batch data for specific is requested, a date must also be provided.
    Returns:
        Dataframe -- batch request for daily candle information for all stocks.
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    if tickers is None:
        url = urlroot + "batch-request-end-of-day-prices?apikey=" + apikey
    elif (tickers is not None) and (date is None):
        raise Exception('For batch query of specific stocks, please specify a date in the format yyyy-mm-dd')
    elif (tickers is not None) and (date is not None):
        tick = ''
        for ticker in tickers:
            tick = tick + ticker + ','
        url = urlroot + "batch-request-end-of-day-prices/" + tick + "?date=" + date + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    if pd.read_json(data).empty is True:
        raise ValueError("Data not found for " + str(tickers) + " on specified date " + date)
    return pd.read_json(data)

def available_markets_and_tickers():
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    return 0

def stock_market_performances():
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    return 0

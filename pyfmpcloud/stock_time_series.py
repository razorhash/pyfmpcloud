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
    return safe_read_json(data)

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
        url = urlroot + 'search?query=' + match + '&limit=' + str(limit) + "&exchange=" + exchange.lower() + '&apikey=' + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def historical_stock_data(ticker, period = None, dailytype = None, last = None, start = None, end = None):
    """Historical stock data API for . From https://fmpcloud.io/documentation#historicalStockData
    
    Input:
        ticker - fx for which you want the historical data
        period - tick periodicity - can be '1min', '5min', '15min', '30min', '1hour'. Defaults to '15min'. Do not use with daily type
        dailytype - can be 'line', 'change'. line chart info for daily price or daily change and volume. Do not use with period.
        last - fx data for last x days. Only works with dailytype. Does not work with period 
        start - start date in the format yyyy-mm-dd. eg: '2018-01-01'
        end - end date in the format yyyy-mm-dd. eg: '2019-01-01'
    Returns:
        Dataframe -- fx stock data
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
    if dailytype == 'line':
        urlhist = urlhist + "serietype=line"
    if last is not None:
        urlhist = urlhist + "&timeseries=" + str(last)
    if (last is None) and (start is not None):
        urlhist = urlhist + "&from=" + start 
    if (last is None) and (end is not None):
        urlhist = urlhist + "&to" + end 
    url = urlhist+ "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    data = safe_read_json(data)
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
    return safe_read_json(data)

def symbol_list():
    """Stocks list API from https://financialmodelingprep.com/developer/docs/#Company-Profile
    
    Input:
        ticker : ticker for which we need the company profile
    Returns:
        Dataframe -- Returns company profile of the requested company (ticker)
    """
    urlroot = settings.get_urlrootfmp()
    apikey = settings.get_apikey()
    url = urlroot + "company/stock/list?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.DataFrame(json.loads(data)['symbolsList'])
    
def company_profile(ticker):
    """Company profile API from https://financialmodelingprep.com/developer/docs/#Symbols-List
    
    Returns:
        DataFrame -- Returns company profile
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    url = urlroot + "company/profile/" + ticker + "?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)
    

def available_markets_and_tickers(markettype = None, marketprices = False):
    """List of available tickers per specified market, and their prices. From https://fmpcloud.io/documentation#availableMarketandTickers
    
    Input:
        marketType : type of market for which we need the available tickers/prices. marketType can be "ETF", "Commodities", "Euronext", "NYSE", "AMEX", "TSX", "Mutual Funds", "Index", "Nasdaq". 
        marketprices : Boolean to indicate if you want the prices of the tickers for the specified markettype.
    Returns:
        Dataframe -- Returns list of available tickers per specified market, and their prices if marketPrices = True
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    
    if markettype is None:
        raise Exception("Please provide marketType. For a list of available options, see function documentation or visit https://fmpcloud.io/documentation#availableMarketandTickers")
    urlmarket = map_markets(markettype.lower(), marketprices)
    url = urlroot + urlmarket + "?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def stock_market_performances(performancetype):
    """Provides an overview of the market performance across specified performance type. https://fmpcloud.io/documentation#stockMarketPerformances
    
    Input:
        performancetype : type of performance for which data is sought. performance type can be "active", "gainers", "losers", "sector", "sector historical", "market hours". 
    Returns:
        Dataframe -- market performance data by specified performance type
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    url = urlroot + map_performance(performancetype.lower()) + "?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def map_markets(markettype, marketPrices):
    marketToApi = {
            "etf" : "available-etfs/",
            "commodities" : "available-commodities/",
            "euronext" : "available-euronext/",
            "nyse" : "availabe-nyse/",
            "amex" : "available-amex/",
            "tsx" : "available-tsx/",
            "index": "available-indexes/",
            "mutual fund": "available-mutual-funds/",
            "nasdaq":"available-nasdaq/",
            }
    
    marketPricesToApi = {
            "etf" : "etf/",
            "commodities" : "commodity/",
            "euronext" : "euronext/",
            "nyse" : "nyse/",
            "amex" : "amex/",
            "tsx" : "tsx/",
            "index": "index/",
            "mutual fund": "mutual_fund/",
            "nasdaq":"nasdaq/",
            }
    if marketPrices == False:
        urlm = "symbol/" + marketToApi[markettype]
    elif marketPrices == True:
        urlm = "quotes/" + marketPricesToApi[markettype]
    return urlm

def map_performance(performancetype):
    performanceToAPI = {
            "active" : "actives",
            "gainers" : "losers",
            "losers" : "gainers",
            "sector" : "sectors-performance",
            "sector historical" : "historical-sectors-performance",
            "market hours" : "market-hours"
            }
    try: 
        urlp = performanceToAPI[performancetype]
    except ValueError:
        raise ValueError("Invalid 'performancetype' value " + performancetype)
    return urlp

def safe_read_json(data):
    if (data.find("Error Message") != -1):
        raise Exception(data[20:-3])
    else:
        return pd.read_json(data)
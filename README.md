# Python wrapper library for the Financial Markets Prep pro (fmpcloud.io)
A python wrapper for the Financial Model Prep API pro (fmpcloud.io) for analysis of public companies

To install please use:

``pip install pyfmpcloud``

This is the first release and includes the following functionalities:

### settings.py

General settings for the library

``set_apikey``: Please set your API Key in this file using the settings.set_apikey([YOUR KEY]). The key can be retrieved from fmpcloud.io by signing up. Default is the 'demo' key
    
``get_apikey``: Get current API key
    
``get_urlroot``: get the root API url for fmpcloud.io
    
``get_urlrootfmp``: get the root API url for financialmodelprep.com
    
### company_valuation.py

Here, you have functions that wrap around the APIs listed in fmpcloud.io (see [fmpcloud.io API documentation](https://fmpcloud.io/documentation)) under Company Valuation. these are:

``rss_feed``

``balance_sheet``
    
``income_statement``
    
``cash_flow_statement``
    
``financial_ratios``
    
``key_metrics``
    
``enterprise_value``
    
``financial_statements_growth``
    
``dcf``
    
``market_capitalization``
    
``rating``
    
``stock_screener``
    
### stock_time_series.py

These contain general functions from fmpcloud.io 's sister API (see [fmpcloud.io API documentation](https://fmpcloud.io/documentation)) under Stock Time Series. these are:

``real_time_quote``: real-time quotes for specified tickers

``ticker_search``: partial matching of tickers based on provided string element

``historical_stock_data``: historical stock data for specified tickers

``batch_request_eod_prices``: batch request for EOD prices. Only accepts an array of strings, even for a single ticker input

``stocks_list``: list of all available tickers on the API

``company_profile``: company profile for the specified ticker

``available_markets_and_tickers``: list of available stocks on the specified market (e.g. Nasdaq), and prices of the tickers on the specified market


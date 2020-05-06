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
    
### info.py

These contain general functions from fmpcloud.io 's sister API (see [financialmodelprep.com API documentation](https://financialmodelingprep.com/developer/docs/))

``stocks_list``: list of all available tickers on the API

``company_profile``: returns the high level company profile


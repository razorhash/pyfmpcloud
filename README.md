# A Python wrapper library for the Financial Model Prep pro (fmpcloud.io)

[![PyPI Latest Release](https://img.shields.io/pypi/v/pyfmpcloud.svg)](https://pypi.org/project/pyfmpcloud/)
[![Package Status](https://img.shields.io/pypi/status/pyfmpcloud.svg)](https://pypi.org/project/pyfmpcloud/)
[![License](https://img.shields.io/pypi/l/pyfmpcloud.svg)](https://github.com/razorhash/pyfmpcloud/blob/master/LICENSE)
![downloads](https://img.shields.io/pypi/dm/pyfmpcloud)

pyfmpcloud is a Python wrapper library for the Financial Model Prep pro API (fmpcloud.io) 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyfmpcloud

```bash
pip install pyfmpcloud --upgrade --no-cache-dir 
```

Alternatively, download and extract the *.tar.gz folder, and run the following command from the 
root directory in your shell:

```bash
make setup
```

## Usage

pyfmpcloud contains a ``settings`` module and four other modules that are the core of the 
pyfmpcloud API wrapper. 


The following sections show the four main modules for pyfmpcloud and their usage with examples. 
Note that the modules are structured in the same way as the API documentation that can be found 
at [fmpcloud.io API documentation](https://fmpcloud.io/documentation). The names of the functions 
within the modules also follow the naming convention on this documentation. This helps with staying
consistent. The four modules and their functions are as follows:

### Settings
```python 
from pyfmpcloud import settings
```
General helper functions to access and update settings for the library environment. These are:

``set_apikey``: Please set your API Key in this file using the settings.set_apikey([YOUR KEY]). The key can be retrieved from fmpcloud.io by signing up. Default is the 'demo' key. Example:
```python 
settings.set_apikey('stringcontainingyourapikey')
```
``get_apikey``: Gets the currently set API key. Default is `demo`
```python
settings.get_apikey()
```
``get_urlroot``: Gets the root API url for fmpcloud.io
```python
settings.get_urlroot()
```
``get_urlrootfmp``: Gets the root API url for fmpcloud's sister API financialmodelprep.com. Good to have but is not currently used in the wrapper.
```python
settings.get_urlrootfmp()
```

### Company Valuation
```python 
from pyfmpcloud import company_valuation as cv
```
Here, you have functions that wrap around the APIs listed in fmpcloud.io (see [fmpcloud.io API documentation](https://fmpcloud.io/documentation)) under Company Valuation. These are:

``rss_feed``: This function returns updates for all filings of public companies, including their filing type (10-Q, 13-F, etc.), their CIK number, and the date and time of the filing. 

```python
cv.rss_feed()
```
``balance_sheet``: This function returns the balance sheet information of the specified ticker. Inputs are: ``ticker``, ``period``(_'annual'_ or _'quarter'_) and ``ftype``(_'full'_ or _'growth'_) 

Examples:

```python
cv.balance_sheet(ticker = 'AAPL', period = 'annual', ftype = 'full')
cv.balance_sheet(ticker = 'AAPL', period = 'annual', ftype = 'growth')
cv.balance_sheet(ticker = 'AAPL', period = 'quarter', ftype = 'full')
cv.balance_sheet(ticker = 'AAPL', period = 'quarter', ftype = 'growth')
```

``income_statement``: This function returns the income statement of the specified ticker. Inputs arguments are: ``ticker``, ``period``(_'annual'_ or _'quarter'_) and ``ftype``(_'full'_, _'growth'_)  

Examples:

```python
cv.balance_sheet(ticker = 'AAPL', period = 'annual', ftype = 'full')
cv.balance_sheet(ticker = 'AAPL', period = 'annual', ftype = 'growth')
cv.balance_sheet(ticker = 'AAPL', period = 'quarter', ftype = 'full')
cv.balance_sheet(ticker = 'AAPL', period = 'quarter', ftype = 'growth')
```

``cash_flow_statement``: This function returns the cash-flow statement of the specified ticker. Inputs are Inputs are: ``ticker``, ``period``(_'annual'_ or _'quarter'_) and ``ftype``(_'full'_ or _'growth'_)

Examples:

```python
cv.cash_flow_statement(ticker = 'AAPL', period = 'annual', ftype = 'full')
cv.cash_flow_statement(ticker = 'AAPL', period = 'annual', ftype = 'growth')
cv.cash_flow_statement(ticker = 'AAPL', period = 'quarter', ftype = 'full')
cv.cash_flow_statement(ticker = 'AAPL', period = 'quarter', ftype = 'growth')
```

``financial_ratios``: This function returns the financial ratios of the specified ticker. ``ttm`` can provide these ratios for the trailing twelve months. Inputs arguments are: ``ticker``, ``period``(_'annual'_ or _'quarter'_) and ``ttm``(``True`` or ``False``)

Examples:

```python
cv.financial_ratios(ticker = 'AAPL', period = 'annual', ttm = True)
cv.financial_ratios(ticker = 'AAPL', period = 'annual', ttm = False)
cv.financial_ratios(ticker = 'AAPL', period = 'quarter', ttm = True)
cv.financial_ratios(ticker = 'AAPL', period = 'quarter', ttm = False)
```   

``key_metrics`` : This function returns the key metrics of the specified ticker. Inputs are: ``ticker`` and  ``period``(_'annual'_ or _'quarter'_)

Examples:

```python
cv.key_metrics(ticker = 'AAPL', period = 'annual')
cv.key_metrics(ticker = 'AAPL', period = 'quarter')
```

``enterprise_value`` : This function returns the enterprise value of the specified ticker. Inputs are: ``ticker`` and  ``period``(_'annual'_ or _'quarter'_)

Examples:

```python
cv.enterprise_value(ticker = 'AAPL', period = 'annual')
cv.enterprise_value(ticker = 'AAPL', period = 'quarter')
```
``financial_statements_growth`` : This function returns the financial statements growth/evolution over time of the specified ticker. Inputs are: ``ticker`` and  ``period``(_'annual'_ or _'quarter'_)

Examples:

```python
cv.financial_statements_growth(ticker = 'AAPL', period = 'annual')
cv.financial_statements_growth(ticker = 'AAPL', period = 'quarter')
```

``dcf`` : This function returns the discounted cashflow value of the specified ticker, over time. Inputs are: ``ticker`` and  ``history``(_'today'_, _'daily'_, _'annual'_ or _'quarter'_)

Examples:

```python
cv.dcf(ticker = 'AAPL', history = 'today')
cv.dcf(ticker = 'AAPL', history = 'daily')
cv.dcf(ticker = 'AAPL', history = 'annual')
cv.dcf(ticker = 'AAPL', history = 'quarter')
```

``market_capitalization`` : This function returns the market capitalization of the specified ticker, over time. Inputs are: ``ticker`` and ``history``(_'today'_, _'daily'_)

Examples:

```python
cv.market_capitalization(ticker = 'AAPL', history = 'today')
cv.market_capitalization(ticker = 'AAPL', history = 'daily')
```

``rating``: This function returns the ratings of the specified ticker, over time. Inputs are: ``ticker`` and ``history``(_'today'_, _'daily'_)

Examples:

```python
cv.rating(ticker = 'AAPL', history = 'today')
cv.rating(ticker = 'AAPL', history = 'daily')
```

``stock_screener`` : A function to screen stocks based on market capitalization, beta, dividend payouts, trading volume and  sector. Also allows you to limit the number of rows returned from the request. The following are the arguments to apply the filter.

``mcgt`` : ``float`` input for **m**arket **c**ap **g**reater **t**han. 
``mclt`` : ``float`` input for **m**arket **c**ap **l**ess **t**han
``bgt`` : ``float`` input for **b**eta **g**reater **t**han
``blt`` : ``float`` input for **b**eta **l**ess **t**han
``divgt`` : ``float`` input for **div**idend **g**reater **t**han
``divlt`` : ``float`` input for **div**idend **l**ess **t**han
``volgt`` : ``float`` input for **vol**ume **g**reater **t**han
``vollt`` : ``float`` input for **vol**ume **l**ess **t**han
``sector`` : ``string`` input for sector. 
``limit`` : ``int`` input for limit of returned rows from the API request

Examples: 

```python 
cv.stock_screener('AAPL', mcgt = 1000000, mclt = 5000000, bgt = 1.2, blt = 2.1)
cv.stock_screener('AAPL', mcgt = 1000000, mclt = 5000000, volgt = 500000, blt = 2.1, divgt = 1)
```
### Stock Time Series
```python 
from pyfmpcloud import stock_time_series as sts
```
These contain functions from fmpcloud.io 's API for Stock Time Series (see [fmpcloud.io API documentation](https://fmpcloud.io/documentation)) under Stock Time Series. these are:

``real_time_quote``: Real-Time Quotes for specified tickers. Input is ``ticker``

Example:
```python 
sts.real_time_quote('AAPL')
```

``ticker_search``: Partial matching of tickers based on provided string element. Inputs are ``match``, ``limit`` and ``exchange``

Examples:
```python
sts.ticker_search(match = 'AA', limit = 100, exchange = 'Nasdaq')
```

``historical_stock_data``: Historical stock data for specified tickers based on specified ``period`` ('1 min', '5min', '15min', '30min' and '1hour', or daily change type ``dailytype`` (_'line'_, _'change'_). ``period`` and ``dailytype`` cannot be used together. If ``dailytype`` is used, you can specify ``start`` and ``end`` dates for your request. Dates are a simple string (**not** a datetime object) in the format yyyy-mm-dd. Alternatively, you can also specify a request for daily prices over the last number of days using ``last``

Examples:

``` python
sts.historical_stock_data('AAPL', period = '1hour')
sts.historical_stock_data('AAPL', dailytype = 'line', start = '2019-04-15', end = '2020-04-15')
sts.historical_stock_data('AAPL', dailytype = 'change', start = '2019-04-15', end = '2020-04-15')
sts.historical_stock_data('AAPL', dailytype = 'change', last = 30)
```

``batch_request_eod_prices``: batch request for EOD prices for a single date (if no date is specified, it will return the EOD prices for the last market close). Only accepts an array of strings, even for a single ``ticker`` request. If tickers are provided, a date **must** be provided. If no ticker is provided, it will return the EOD prices for all tickers.  ``date`` is a simple string (**not** a datetime object) in the format yyyy-mm-dd

Examples:

``` python
sts.batch_request_eod_prices()
sts.batch_request_eod_prices(['AAPL'], date='2020-04-15')
sts.batch_request_eod_prices(date='2020-04-15')
sts.batch_request_eod_prices(['AAPL', 'FB', 'MSFT'], date='2020-04-15')
```

``stocks_list``: List of all available tickers. 

Example: 
```python
sts.stock_list()
```

``company_profile``: Company profile for the specified ticker

Example: 
```python
sts.company_profile('AAPL')
```

``available_markets_and_tickers``: List of available stocks on the specified market (e.g. Nasdaq), and prices of the tickers on the specified market. Inputs are ``markettype`` ('_ETF_','_Commodities_','_Euronext_','_NYSE_','_AMEX_','_TSX_','_Mutual Funds_','_Index_' or '_Nasdaq_') and a boolean ``marketprices` (``True or ``False``) to indicate if prices of the tickers for the specified ``markettypes`` are sought.

Examples:
```python
sts.available_markets_and_tickers(markettype = 'Nasdaq')
sts.available_markets_and_tickers(markettype = 'Nasdaq', marketprices = True)
```

``stock_market_performances``: Overview of the market performance across specified performance type, such as by sector, or by largest gainers. Input is ``performancetype``('_active_','_gainers_','_losers_','_sector_','_sector historical_', 'market hours')

Examples:
```python
sts.stock_market_performances(performancetype = 'active')
sts.stock_market_performances(performancetype = 'market hours')
```
### Forex
```python 
from pyfmpcloud import forex as fx
```
These contain functions from fmpcloud.io 's API for Forex  (see fmpcloud.io API documentation). these are:

``forex_realtime_quote``: Real-time quotes for specified fx tickers. You can request the list of forex, their prices, or both through the ``fxtype`` (_'list'_, _'price'_, _'both'_) argument.

Examples:
```python 
fx.forex_realtime_quote(fxtype = 'list')
fx.forex_realtime_quote(fxtype = 'price')
fx.forex_realtime_quote(fxtype = 'both')
```

``forex_historical_data``: Historical fx data for specified tickers based on specified ``period`` ('1 min', '5min', '15min', '30min' and '1hour', or daily change type ``dailytype`` (_'line'_, _'change'_). ``period`` and ``dailytype`` cannot be used together. If ``dailytype`` is used, you can specify ``start`` and ``end`` dates for your request. Dates are a simple string (**not** a datetime object) in the format yyyy-mm-dd. Alternatively, you can also specify a request for daily fx prices over the last number of days using ``last``

Examples:

``` python
fx.forex_historical_data('EURUSD', period = '1hour')
fx.forex_historical_data('EURUSD', dailytype = 'line', start = '2019-04-15', end = '2020-04-15')
fx.forex_historical_data('EURUSD', dailytype = 'change', start = '2019-04-15', end = '2020-04-15')
fx.forex_historical_data('EURUSD', dailytype = 'change', last = 30)
```

### Crypto
```python 
from pyfmpcloud import crypto as cp
```
These contain functions from fmpcloud.io 's API for Crypto  (see fmpcloud.io API documentation). these are:

``crypto_realtime_quote``: Real-time quotes for specified crypto tickers. You can request the list of crypto or their prices through the ``cryptotype`` (_'list'_, _'price'_) argument.

Examples:
```python 
cp.crypto_realtime_quote(fxtype = 'list')
cp.crypto_realtime_quote(fxtype = 'price')
```

``crypto_historical_data``: Historical crypto data for specified tickers based on specified ``period`` ('1 min', '5min', '15min', '30min' and '1hour', or daily change type ``dailytype`` (_'line'_, _'change'_). ``period`` and ``dailytype`` cannot be used together. If ``dailytype`` is used, you can specify ``start`` and ``end`` dates for your request. Dates are a simple string (**not** a datetime object) in the format yyyy-mm-dd. Alternatively, you can also specify a request for daily fx prices over the last number of days using ``last``

Examples:

``` python
cp.crypto_historical_data('BTCUSD', period = '1hour')
cp.crypto_historical_data('BTCUSD', dailytype = 'line', start = '2019-04-15', end = '2020-04-15')
cp.crypto_historical_data('BTCUSD', dailytype = 'change', start = '2019-04-15', end = '2020-04-15')
cp.crypto_historical_data('BTCUSD', dailytype = 'change', last = 30)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

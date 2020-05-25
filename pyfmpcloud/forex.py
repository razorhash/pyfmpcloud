from urllib.request import urlopen
import pandas as pd
from pyfmpcloud import settings

def forex_realtime_quote(fxtype):
    """Forex Real time quotes including list of available fx, their prices and a combination function to return both. From https://fmpcloud.io/documentation#forex
    
    Input:
        fxtype : can be 'list', 'price' or 'both'
    Returns:
        list of available fx, their prices or both
    """        
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    if fxtype == 'both':
        urlfx = "fx?apikey="
    elif fxtype == 'list':
        urlfx = "symbol/available-forex-currency-pairs?apikey="
    elif fxtype == 'price':
        urlfx = "quotes/forex?apikey="
    else:
        raise KeyError("Invalid fxtype " + fxtype)
    url = urlroot + urlfx + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)
    
def forex_historical_data(ticker, period = None, dailytype = None, last = None, start = None, end = None):
    """Forex Historical data API for partial matching of stocks over specified exchange. From https://fmpcloud.io/documentation#historicalStockData
    
    Input:
        ticker - company for which you want the historical stock data. for complete list of fx, use forex.forex_realtime_quote(fxtype = 'list')
        period - tick periodicity - can be '1min', '5min', '15min', '30min', '1hour'. Defaults to '15min'. Do not use with daily type
        dailytype - can be 'line', 'change'. line chart info for daily stock or daily change and volume. Do not use with period.
        last - stock data for last x days. Only works with dailytype. Does not work with period 
        start - start date in the format yyyy-mm-dd. eg: '2018-01-01'
        end - end date in the format yyyy-mm-dd. eg: '2019-01-01'
    Returns:
        Dataframe -- historical fx data
    """
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    if ((dailytype is not None) or (last is not None)) and (period is not None):
        raise Exception(" 'period' and 'dailytype' cannot be set on the same call. Please choose either, not both. 'last' can only be set with 'dailytype'")
    if dailytype is not None:
        urlhist = urlroot + 'historical-price-full/' + ticker.upper() + '?'
    elif period is not None:
        urlhist = urlroot + 'historical-chart/' + period + '/' + ticker.upper() + '?'
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

def safe_read_json(data):
    if (data.find("Error Message") != -1):
        raise Exception(data[20:-3])
    else:
        return pd.read_json(data)

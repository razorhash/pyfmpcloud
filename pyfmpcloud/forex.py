from urllib.request import urlopen
import pandas as pd
from pyfmpcloud import settings

def forex_realtime_quote(fxtype = 'list'):
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
    return pd.read_json(data)
    
def forex_historical_data():
    return 0

def get_forex_list_url():
    urlfx = "fx?apikey="
    return urlfx
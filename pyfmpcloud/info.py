# -*- coding: utf-8 -*-
from urllib.request import urlopen
import pandas as pd
from pyfmpcloud import settings

def stocks_list():
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
    return pd.read_json(data)
    
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
    return pd.read_json(data)
    
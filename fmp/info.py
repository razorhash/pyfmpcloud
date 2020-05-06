# -*- coding: utf-8 -*-
from urllib.request import urlopen
import pandas as pd
from fmp import settings

def stocks_list():
    """Stocks list API from https://financialmodelingprep.com/developer/docs/#Company-Profile
    
    Input:
        ticker : ticker for which we need the company profile
    Returns:
        Dataframe -- Returns company profile of the requested company (ticker)
    """      
    urlrootfmp = settings.get_urlrootfmp()
    url = urlrootfmp + "company/stock/list"
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)
    
def company_profile(ticker):
    """Company profile API from https://financialmodelingprep.com/developer/docs/#Symbols-List
    
    Returns:
        DataFrame -- Returns company profile
    """        
    urlrootfmp = settings.get_urlrootfmp()
    url = urlrootfmp + "company/profile/" + ticker
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return pd.read_json(data)
    
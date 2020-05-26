from urllib.request import urlopen
import pandas as pd
from pyfmpcloud import settings

def form_list():
    """Returns all names of companies and their CIK numbers. From https://fmpcloud.io/documentation#thirteenFormList
    
    Returns:
        list of available companies and their CIK numbers 
    """        
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    url = urlroot + "cik_list?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def form_nametocik(company):
    """Returns CIK number for specified company. Allows partial matching of names. From https://fmpcloud.io/documentation#thirteenFormName
    
    Input:
        company : Name of the company for which you'd like the CIK 
    Returns:
         CIK number for specified company
    """        
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    url = urlroot + "cik-search/" + company + "?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def form_ciktoname(cik):
    """Returns company name for specified CIK number. From https://fmpcloud.io/documentation#thirteenFormCik
    
    Input:
        cik : CIK number for which you'd like the company name
    Returns:
        Company name for specified company
    """        
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    url = urlroot + "cik/" + cik + "?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def form(cik, year):
    """Returns form 13F for specified CIK number. From https://fmpcloud.io/documentation#thirteenForm
    
    Input:
        cik : CIK number for which you'd like the 13F form
        year = year for which you'd like the 13F form.
    Returns:
        Form 13F for specified company
    """        
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    url = urlroot + "form-thirteen/" + cik + "?year=" + year + "&apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def cusip_mapper(cusip):
    """Returns the company name for specified CUSIP number. From https://fmpcloud.io/documentation#cusipMapper
    
    Input:
        cusip : CUSIP number for which you'd like the company name
    Returns:
        company name for specified CUSIP number
    """        
    urlroot = settings.get_urlroot()
    apikey = settings.get_apikey()
    url = urlroot + "cusip/" + cusip + "?apikey=" + apikey
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return safe_read_json(data)

def safe_read_json(data):
    if (data.find("Error Message") != -1):
        raise Exception(data[20:-3])
    else:
        return pd.read_json(data)
from fmpapi import company_valuation 
#import json 
#import pandas as pd

# print("Current Directory is " + os.getcwd())
# cfg = configparser.ConfigParser()
# cfg.read('config.ini')
# apikey = cfg['API']['api_key']
# urlroot = cfg['API']['url_root']

thisjson = company_valuation.cash_flow_statement('AAPL', period = 'quarter', ftype = 'growth')
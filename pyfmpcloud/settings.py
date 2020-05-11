# -*- coding: utf-8 -*-
import configparser
import os

cfile = os.path.join(os.path.dirname(__file__), 'config.ini')
cfg = configparser.ConfigParser()
cfg.read(cfile)

try:
    cfg.has_section('API')
except:
    raise Exception('Config File was not read.')
    
def get_urlroot():
    urlroot = cfg['API']['url_root']
    return urlroot

def get_urlrootfmp():
    urlrootfmp = cfg['API']['url_root_fmp']
    return urlrootfmp

def get_apikey():
    apikey = cfg['API']['api_key']
    return apikey

def set_apikey(apikey):
    cfg['API']['api_key'] = apikey
    with open(cfile, 'w') as configfile:
        cfg.write(configfile)

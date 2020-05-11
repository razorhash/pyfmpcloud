# -*- coding: utf-8 -*-
import configparser
import sys
site_packages = next(p for p in sys.path if 'pyfmpcloud' in p)

cfile = site_packages + '/config.ini'
cfg = configparser.ConfigParser()
cfg.read(cfile)
#cfile = 'config.ini'

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

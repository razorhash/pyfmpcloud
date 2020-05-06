# -*- coding: utf-8 -*-
import configparser

cfile = 'config.ini'

def get_urlroot():
    cfg = configparser.ConfigParser()
    cfg.read(cfile)
    urlroot = cfg['API']['url_root']
    return urlroot

def get_urlrootfmp():
    cfg = configparser.ConfigParser()
    cfg.read(cfile)
    urlrootfmp = cfg['API']['url_root_fmp']
    return urlrootfmp

def get_apikey():
    cfg = configparser.ConfigParser()
    cfg.read(cfile)
    apikey = cfg['API']['api_key']
    return apikey

def set_apikey(apikey):
    cfg = configparser.ConfigParser()
    cfg.read(cfile)
    cfg['API']['api_key'] = apikey
    with open(cfile, 'w') as configfile:
        cfg.write(configfile)
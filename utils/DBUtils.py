'''
Created on 7 Nov 2017

@author: DEV-SYB-AF
'''
import pymysql
import configparser

from utils import Constant

config = configparser.ConfigParser()
config.read(Constant.CONFIG_PATH)

def db_connect():
    db_host = config['DATABASE']['db_host']
    db_username = config['DATABASE']['db_username']
    db_password = config['DATABASE']['db_password']
    db_name = config['DATABASE']['db_name']
    db = pymysql.connect(db_host, db_username, db_password, db_name)
    return db
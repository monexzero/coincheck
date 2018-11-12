import time
import hmac
import hashlib
import requests
import json
from coincheck.utils import make_header
import simplejson as json

"""
document: https://coincheck.com/documents/exchange/api
"""
class Account(object):
    
    def __init__(self,
                 access_key=None,
                 secret_key=None):
        self.access_key = access_key
        self.secret_key = secret_key

    def get_info(self):
        ''' show user information
        '''

        url= 'https://coincheck.com/api/accounts'
        headers = make_header(url,
                              access_key = self.access_key,
                              secret_key = self.secret_key)

        r = requests.get(url,
                         headers = headers)
        return json.loads(r.text)
    
    def get_balance(self):
        ''' confirm balance
        '''
        url = 'https://coincheck.com/api/accounts/balance'
        headers = make_header(url,
                              access_key = self.access_key,
                              secret_key = self.secret_key)
        r = requests.get(url,
                         headers = headers)
        return json.loads(r.text)

    def get_deposits(self, currency="BTC"):
        ''' get deposit money
        '''
        url = 'https://coincheck.com/api/deposit_money'
        params = {"currency": currency}
        headers = make_header(url,
                              access_key = self.access_key,
                              secret_key = self.secret_key,
                              params=params)
        r = requests.get(url,
                         headers = headers,
                         params=params,
                         )
        return json.loads(r.text)

    def get_withdraws(self):
        ''' get withdraws
        '''
        url = 'https://coincheck.com/api/withdraws'
        headers = make_header(url,
                              access_key = self.access_key,
                              secret_key = self.secret_key)
        r = requests.get(url,
                         headers = headers,
                         )
        return json.loads(r.text)

    def get_sends(self, currency="BTC"):
        ''' get send money
        '''
        url = 'https://coincheck.com/api/send_money'
        params = {"currency": currency}
        headers = make_header(url,
                              access_key = self.access_key,
                              secret_key = self.secret_key,
                              params=params,
                              )
        r = requests.get(url,
                         headers = headers,
                         params=params,
                         )
        return json.loads(r.text)
    

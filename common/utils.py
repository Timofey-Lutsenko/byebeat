import bybit
import requests
import json
from datetime import datetime


from api_config import *


def get_server_time():
    """
    Depending on the response code
    :returns:
        -current BYBIT server time.
        -False
    """
    req = requests.get(BYBIT_SERVER_TIME)
    if req.status_code == 200:
        data_as_dict = json.loads(req.text)
        server_time = data_as_dict['result']
        return server_time.get('serverTime')
    if req.status_code == 403:
        print('Access denied')
        return False
    if req.status_code == 404:
        print('Request path not found')
        return False
    else:
        print('Unknown status code.')
        return False


def receive_window_checker():
    """
    :return: TRUE if the time of the local machine matches the connection conditions.
    """
    if get_server_time():
        server_time = get_server_time()
        local_time = datetime.now().timestamp() + 1000
        connection_window = [
            server_time - 5000,
            server_time + 1000
        ]
        if connection_window[0] <= local_time <= connection_window[1]:
            return True
        else:
            return False


def get_candle():
    """
    Function returns array (list of arrays if param 'limit' > 1) with next data:
    Start time          (type int)      (WARNING!For correct subsequent work with the field, it must be divided by 1000)
    open	            (type float)	Open price
    high	            (type float)	High price
    low	                (type float)	Low price
    close	            (type float)	Close price
    volume	            (type float)	Trading volume
    endTime	            (type int)	    End time, unit in millisecond
    quoteAssetVolume    (type float)	Quote asset volume
    trades	            (type int)	    Number of trades
    takerBaseVolume	    (type float)	Taker buy volume in base asset
    takerQuoteVolume    (type float)    Taker buy volume in quote asset

    Required parameters to be passed:
        -symbol(str)
        -interval(str)
        Interval options:
            -1m/3m/5m/15m/30m - 1/3/5/15/30 minutes
            -1h/2h/4h/6h/12h - 1/2/4/6/12 hours
            -1d - 1 day
            -1w - 1 week
            -1M - 1 month
        Optional requirements:
            -limit(int)	default 1000 max 10,000
            -startTime unit in millisecond
            -endTime unit in millisecond
    """
    # TODO input form for UI desktop.
    params = {
        'symbol': SYMBOL,
        'interval': '15m',
        'limit': '1'
    }
    req = requests.get(CANDLE, params)
    data_as_dict = json.loads(req.text)
    if int(params['limit']) == 1:
        return data_as_dict['result']
    """
    potentially useful
    else:
        for el in data_as_dict['result']:
            print(el)
    """


def available_funds():
    """
    :return: available balance of connected account.
    """
    client = bybit.bybit(test=False, api_key=API_KEY, api_secret=API_SECRET)
    account = client.Wallet.Wallet_getBalance(coin="BTC").result()[0]['result']['BTC']
    available_balance = account['available_balance']
    # potentially useful
    wallet_balance = account['wallet_balance']
    return available_balance


def percent_calculation(percent):
    """
    :param percent: percent as integer.
    Сonverts to the form of hundredths (decimal) parts
    :return: Transferred percentage of the amount.
    """
    # funds = available_funds()
    # TEST
    funds = 1337.7331
    target_percent = funds * percent / 100
    return target_percent

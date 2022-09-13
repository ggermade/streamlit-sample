from pycoingecko import CoinGeckoAPI
import pandas as pd

import requests as re
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import streamlit as st

cg = CoinGeckoAPI()

def get_token_history(id, date_list, localization="false"):
    try:
        highs = []
        lows = []
        vols = []
        caps = []
        for date in date_list:
            response = cg.get_coin_by_id(id=id,date=date,localization=localization)
            highs.append(response['market_data']['high_24h']['usd'])
            lows.append(response['market_data']['low_24h']['usd'])
            vols.append(response['market_data']['total_volume']['usd'])
            caps.append(response['market_data']['market_cap']['usd'])
        
        df = pd.DataFrame(list(zip(date_list, highs, lows, vols, caps)), columns=['date','high','low','vol','mcap'])
        # response = re.get(request_url)
        # data = response.json()
        return df
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


domain = 'http://api.coingecko.com/api/v3'
coinlist_endpoint = '/coins/list'
coins_id_history_endpoint = '/coins/{id}/history'

def get_token_by_name(token, domain=domain, endpoint=coinlist_endpoint):

    try:
        response = re.get(domain+endpoint)
        coin_list = response.json()

        for ele in coin_list:
                if ele['symbol'] == token or ele['symbol'] == token.lower():
                    return ele
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def get_token_history_at_date(token_id,date,localization="false"):
    try:
        request_url = domain+coins_id_history_endpoint.format(id=token_id)+'?'+'date='+date+'&'+'localization='+localization
        print(request_url)
        response = re.get(request_url)
        data = response.json()
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


    
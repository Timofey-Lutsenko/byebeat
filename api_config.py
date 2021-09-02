"""
API PART includes API key, secret and list
of permissions
"""

API_KEY = 'ZlYriJdUpRRTw83Wyn'
API_SECRET = 'tXwQy23RP5wK9on6YLLxg3NMxyGgWcDLmXIj'
PERMISSIONS = [
    'Контракты - Позиции Ордера',
    'СПОТ - ТОРГОВАТЬ',
    'Кошелек - Перевод с аккаунта',
    'Перевод с субаккаунта',
    {'Только для чтения': False}
    ]


# Request addresses
BYBIT_SERVER_TIME = 'https://api.bybit.com/spot/v1/time'
CANDLE = 'https://api.bybit.com/spot/quote/v1/kline'


# Server restrictions on requests
RATE_LIMITS = {
    'get_method': {
        'req_per_sec_cont_for_2_min': 50,
        'req_per_sec_cont_for_5_sec': 70
    },
    'post_method': {
        'req_per_sec_cont_for_2_min': 20,
        'req_per_sec_cont_for_5_sec': 50
    }
}

# Optional settings part+
SYMBOL = 'BTCUSDT'

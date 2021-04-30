import hug

from . import repository

@hug.get('/{symbol}')
def getQuote(symbol: hug.types.text):
    return repository.getQuote(symbol)

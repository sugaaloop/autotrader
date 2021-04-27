import hug

from . import entityRepo

@hug.get('/{symbol}')
def getQuote(symbol: hug.types.text):
    return entityRepo.getQuote(symbol)

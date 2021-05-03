from get_todayPrices import getEndOfDay
from get_fundamentals import getTodayFundamentals
from get_fundamentals_statements import getTodayFundamentalsStatements
from insert_prices import insertPrices
from insert_fundamentals import insertFundamentals
from tickers import tickers
import json

startDate = '2021-04-16'
endDate = '2021-04-23'
apiToken ='03e7b05ae58a0f4a92b43326ca36a4ebfff91dfd'

for ticker in tickers:

    endOfDay = getEndOfDay(ticker, startDate, endDate, apiToken)
    fundamentals = getTodayFundamentals(ticker, startDate, endDate, apiToken)

    for i in endOfDay:
        try:
            index = endOfDay.index(i)
            insertPrices(ticker, startDate, endDate, apiToken, index, endOfDay, fundamentals)
        except Exception as e:
            print('no data - prices: ', e)

for ticker in tickers:

    fundamentalsStatements = getTodayFundamentalsStatements(ticker, startDate, endDate, apiToken)

    filename = 'data/'+ticker+'_statement.json'
    with open(filename, 'w') as outfile:
        json.dump(fundamentalsStatements, outfile, indent=4)

    print('============================ new ticker',ticker,' \n')
    for i in fundamentalsStatements:

        #try:
            index = fundamentalsStatements.index(i)
            insertFundamentals(ticker, startDate, endDate, apiToken, index, fundamentalsStatements)
        #except Exception as e:
         #   print('no data - funda: ', e)




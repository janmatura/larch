from insert_prices import insertPrices


tickers = ('AAPL', 'BA', 'CAT', 'MSFT')

startDate = '2020-12-23'
endDate = '2020-12-23'
#ticker = 'AAPL'
apiToken ='03e7b05ae58a0f4a92b43326ca36a4ebfff91dfd'

for ticker in tickers:

    insertPrices(ticker, startDate, endDate, apiToken)


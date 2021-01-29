from insert_prices import insertPrices
from insert_fundamentals import insertFundamentals
from datetime import date, timedelta


tickers = ('AAPL', 'BA', 'CAT', 'MSFT')
today = (date.today() - timedelta(days=3)).strftime("%Y-%m-%d")
print('\n =====================================================\n Good morning of ',today, '. Continue in being greatest!\n')


startDate = today
endDate = today
apiToken ='03e7b05ae58a0f4a92b43326ca36a4ebfff91dfd'

for ticker in tickers:

    insertPrices(ticker, startDate, endDate, apiToken)
    insertFundamentals(ticker, startDate, endDate, apiToken)

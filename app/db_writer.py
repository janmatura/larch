from insert_prices import insertPrices
from insert_fundamentals import insertFundamentals
from eval_pe import peChange
from eval_pea import peAverage
from datetime import date, timedelta
from tickers import tickers

yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
today = date.today().strftime("%Y-%m-%d")
print('\n =====================================================\n Good morning of ',today, '. Continue in being greatest!\n')


startDate = yesterday
endDate = yesterday
apiToken ='03e7b05ae58a0f4a92b43326ca36a4ebfff91dfd'

for ticker in tickers:

    insertPrices(ticker, startDate, endDate, apiToken)
    insertFundamentals(ticker, startDate, endDate, apiToken)
    peChange(ticker)
    peAverage(ticker)

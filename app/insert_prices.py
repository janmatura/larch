from get_todayPrices import getEndOfDay
from get_fundamentals import getTodayFundamentals
import pg8000
import json

def insertPrices(ticker, startDate, endDate, apiToken, index = 0, endOfDay = 0, fundamentals = 0):

    if (endOfDay or fundamentals) == 0:
        endOfDay = getEndOfDay(ticker, startDate, endDate, apiToken)
        fundamentals = getTodayFundamentals(ticker, startDate, endDate, apiToken)
        if endOfDay == []:
            print('Prices - empty;')
            return

        if fundamentals == []:
            print('Fundamentals - empty;')
            return


    date = str(endOfDay[index]['date'])
    open = endOfDay[index]['open']
    close = endOfDay[index]['close']
    low = endOfDay[index]['low']
    high = endOfDay[index]['high']
    peRatio = fundamentals[index]['peRatio']
    pbRatio = fundamentals[index]['pbRatio']

    print(ticker, date)

    columns = 'ticker, date, open, close, low, high, peRatio, pbRatio'
    values = "'{ticker}', '{date}', {open}, {close}, {low}, {high}, {peRatio}, {pbRatio}"  \
        .format(ticker=ticker, date=date, open=open, close=close, low=low, high=high, peRatio=peRatio, pbRatio=pbRatio)

    sql = "insert into ticker_ohlc({columns}) values({values}) ON CONFLICT (ticker, date) DO NOTHING;" .format(columns=columns, values=values)

    con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')

    con.run(sql)
    con.commit()


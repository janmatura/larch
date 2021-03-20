import pg8000
from datetime import date, timedelta

def peDecline():
    ticker = 'AAPL'
    today = date.today()
    evalDate = (today - timedelta(days=10)).strftime("%Y-%m-%d")
    sql = f"select peratio from ticker_ohlc where date >= '{evalDate}' and ticker = '{ticker}' order by date asc;"
    con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    peArray = []
    for i in row:
        peArray.append(float(i[0]))
    print("P/E`s Array:", peArray)


peDecline()
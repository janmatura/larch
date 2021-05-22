import pg8000
from datetime import date, timedelta
from tickers import tickers

def peAverage(ticker):

    today = date.today()
    todayInsert = today.strftime("%Y-%m-%d")
    #todayInsert = (today - timedelta(days=2)).strftime("%Y-%m-%d")
    evalDate = (today - timedelta(days=774)).strftime("%Y-%m-%d") # 3 years
    #print('evaldate',evalDate)
    sql = f"select peratio from ticker_ohlc where date >= '{evalDate}' and ticker = '{ticker}' order by date asc;"
    con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    peArray = []
    print(todayInsert)

    try:
        for i in row:
            peArray.append(float(i[0]))

        peMean = sum(peArray)/len(peArray)

        sql = f"update evaluation set pe_a ={peMean} where ticker='{ticker}' and date='{todayInsert}';"

        con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')
        con.run(sql)
        con.commit()
    except Exception as e:
        print(f'Error - Evaluation pe_a on ticker {ticker}. Exception: {e} Pe Array: {peArray} .')

for i in tickers:
    peAverage(i)


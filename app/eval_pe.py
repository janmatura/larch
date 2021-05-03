import pg8000
from datetime import date, timedelta

def peChange(ticker):

    today = date.today()
    todayInsert = today.strftime("%Y-%m-%d")
    evalDate = (today - timedelta(days=130)).strftime("%Y-%m-%d")
    print('evaldate',evalDate)
    sql = f"select peratio from ticker_ohlc where date >= '{evalDate}' and ticker = '{ticker}' order by date asc;"
    con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    peArray = []

    try:
        for i in row:
            peArray.append(float(i[0]))
        print(f'{ticker} peArray:', peArray)
        startList = peArray[0:9]
        endList = peArray[-10:-1]
        startMean = sum(startList)/len(startList)
        endMean = sum(endList)/len(endList)

        change = round((endMean - startMean)/(startMean/100), 2)
        print(f'{ticker} p/e change: {change} % ;')

        columns = 'ticker, date, pe_change_130_p'
        values = f"'{ticker}', '{todayInsert}', {change}"

        sql = f"insert into evaluation({columns}) values({values}) ON CONFLICT (ticker, date) DO NOTHING;"

        con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')
        con.run(sql)
        con.commit()
    except:
        print(f'Evaluation error on ticker {ticker}. Pe Array: {peArray} .')

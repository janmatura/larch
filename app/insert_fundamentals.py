from get_fundamentals_statements import getTodayFundamentalsStatements
from json_helpers import parseFundamentalValue
import pg8000


def insertFundamentals(ticker, startDate, endDate, apiToken, index = 0, fundamentals = 0):

    if fundamentals == 0:
        fundamentals = getTodayFundamentalsStatements(ticker, startDate, endDate, apiToken)
        if fundamentals == []:
            return

    global jdate, jquarter, jroa, jpiotroskiFScore, jeps, jrevenue, jgrossProfit, jebt, jebitda, jtotalAssets, jsharesBasic
    try:
        jdate = str(fundamentals[index]['date'])
        jquarter = fundamentals[index]['quarter']
        jroa = parseFundamentalValue(fundamentals, index, 'overview', 'roa')
        jpiotroskiFScore = parseFundamentalValue(fundamentals, index, 'overview', 'piotroskiFScore')
        jeps = parseFundamentalValue(fundamentals, index, 'incomeStatement', 'eps')
        jrevenue = parseFundamentalValue(fundamentals, index, 'incomeStatement', 'revenue')
        jgrossProfit = parseFundamentalValue(fundamentals, index, 'incomeStatement', 'grossProfit')
        jebt = parseFundamentalValue(fundamentals, index, 'incomeStatement', 'ebt')
        jebitda = parseFundamentalValue(fundamentals, index, 'incomeStatement', 'ebitda')
        jtotalAssets = parseFundamentalValue(fundamentals, index, 'balanceSheet', 'totalAssets')
        jsharesBasic = parseFundamentalValue(fundamentals, index, 'balanceSheet', 'sharesBasic')

    except Exception as e:
       print(f'FundaInsert error on ticker: {ticker} ', e)

    columns = 'ticker, quarter, date, roa, piotroskiFScore, eps, revenue, grossProfit, ebt, ebitda, totalAssets, sharesBasic'
    values = "'{ticker}', '{quarter}', '{date}', {roa}, {piotroskiFScore}, {eps}, {revenue}, {grossProfit}, {ebt}, {ebitda}, {totalAssets}, {sharesBasic}"  \
        .format(ticker=ticker,
                quarter=jquarter,
                date=jdate,
                roa=jroa,
                piotroskiFScore=jpiotroskiFScore,
                eps=jeps,
                revenue=jrevenue,
                grossProfit=jgrossProfit,
                ebt=jebt,
                ebitda=jebitda,
                totalAssets=jtotalAssets,
                sharesBasic=jsharesBasic,
                )

    sql = "insert into ticker_funda({columns}) values({values}) ON CONFLICT (ticker, date) DO NOTHING;;" .format(columns=columns, values=values)

    con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')

    con.run(sql)
    con.commit()

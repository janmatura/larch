from get_fundamentals_statements import getTodayFundamentalsStatements
from json_helpers import parseFundamentalValue
import pg8000


def insertFundamentals(ticker, startDate, endDate, apiToken, index = 0, fundamentals = 0):

    if fundamentals == 0:
        fundamentals = getTodayFundamentalsStatements(ticker, startDate, endDate, apiToken)
        print('json', fundamentals)
        if fundamentals == []:
            print('Fundamentals statements- empty;')
            return

    print('Fundas not empty;')
    global jdate, jquarter, jroa, jpiotroskiFScore, jeps, jrevenue, jgrossProfit, jebt, jebitda, jtotalAssets, jsharesBasic, jdebtCurrent
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
        jdebtCurrent = parseFundamentalValue(fundamentals, index, 'balanceSheet', 'debtCurrent')

    except Exception as e:
       print('no data - fundaInsert: ', e)

    columns = 'ticker, quarter, date, roa, piotroskiFScore, eps, revenue, grossProfit, ebt, ebitda, totalAssets, sharesBasic, debtCurrent'
    values = "'{ticker}', '{quarter}', '{date}', {roa}, {piotroskiFScore}, {eps}, {revenue}, {grossProfit}, {ebt}, {ebitda}, {totalAssets}, {sharesBasic}, {debtCurrent}"  \
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
                debtCurrent=jdebtCurrent
                )

    sql = "insert into ticker_funda({columns}) values({values});" .format(columns=columns, values=values)
    print(sql)

    con = pg8000.connect('jan', 'localhost', 'larchdata', 5432, '551177ac')

    con.run(sql)
    con.commit()

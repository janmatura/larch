import requests
import json
import datetime

startDate = '2020-12-21'
endDate = '2020-12-22'
ticker = 'jnj'
apiToken ='03e7b05ae58a0f4a92b43326ca36a4ebfff91dfd'


def getTodayFundamentals(ticker, startDate, endDate, apiToken):

    # ugly hack because of tiingo getting fundamentals 1 day delayed compared to daily prices.
    startNew = datetime.datetime.strftime(datetime.datetime.strptime(startDate, "%Y-%m-%d") + datetime.timedelta(days=1), "%Y-%m-%d")
    endNew = datetime.datetime.strftime(datetime.datetime.strptime(endDate, "%Y-%m-%d") + datetime.timedelta(days=1), "%Y-%m-%d")


    endpoint ="https://api.tiingo.com/tiingo/fundamentals/{ticker}/daily?token={token}&startDate={startDate}&endDate={endDate}"\
        .format(token=apiToken,
                ticker=ticker,
                startDate=startNew,
                endDate=endNew)

    headers = {
            'Content-Type': 'application/json',
            }

    requestResponse = requests.get(endpoint, headers=headers)

    resFundamentals = requestResponse.json()


    filename = 'data/{ticker}Funda.json' .format(ticker=ticker)
    with open(filename, 'w') as json_file:
        json.dump(resFundamentals, json_file)

    return resFundamentals

getTodayFundamentals(ticker,startDate, endDate, apiToken)



import requests

startDate = '2020-12-21'
endDate = '2020-12-22'
ticker = 'jnj'
apiToken ='03e7b05ae58a0f4a92b43326ca36a4ebfff91dfd'


def getEndOfDay(ticker, startDate, endDate, apiToken):

    endpoint ="https://api.tiingo.com/tiingo/daily/{ticker}/prices?token={token}&startDate={startDate}&endDate={endDate}"\
        .format(token=apiToken,
                ticker=ticker,
                startDate=startDate,
                endDate=endDate)

    headers = {
            'Content-Type': 'application/json',
            }

    requestResponse = requests.get(endpoint, headers=headers)

    resPrices = requestResponse.json()

    return resPrices




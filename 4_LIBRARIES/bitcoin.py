'''
In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, n,   that they would like to buy.
  If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
  which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
  Be sure to catch any exceptions, as with code like:
        import requests

        try:
            ...
        except requests.RequestException:
            ...

# Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.
'''


import sys               # Command-Line Arguments
import requests          # ??????????????????????


# Defining main function
def main():
    arg = ValidateInput()
    rate = CoinbaseRate()
    value = rate * arg
    print(f"${value:,.4f}")

# Defining sub function
def ValidateInput():

    if   len(sys.argv) == 2:                                 # command line must have 1 argument
        try:
            arg = float(sys.argv[1])
            return arg
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

def CoinbaseRate():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        r = r.json()

        rate = r['bpi']['USD']['rate_float']
        return rate
    except requests.RequestException:
        pass

if __name__=="__main__":
    main()

'''
Note that CoinDesk’s API returns a JSON response like:
{
   "time":{
      "updated":"May 2, 2022 15:27:00 UTC",
      "updatedISO":"2022-05-02T15:27:00+00:00",
      "updateduk":"May 2, 2022 at 16:27 BST"
   },
   "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
   "chartName":"Bitcoin",
   "bpi":{
      "USD":{
         "code":"USD",
         "symbol":"&#36;",
         "rate":"38,761.0833",
         "description":"United States Dollar",
         "rate_float":38761.0833
      },
      "GBP":{
         "code":"GBP",
         "symbol":"&pound;",
         "rate":"30,827.6198",
         "description":"British Pound Sterling",
         "rate_float":30827.6198
      },
      "EUR":{
         "code":"EUR",
         "symbol":"&euro;",
         "rate":"36,800.2764",
         "description":"Euro",
         "rate_float":36800.2764
      }
   }
}
'''


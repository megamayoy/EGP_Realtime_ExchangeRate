import requests
from datetime import date

class CurrencyConverterInterface:

    """ Connects to the currency converter API to send GET requests and get responses
          for more information about the API, visit  https://www.currencyconverterapi.com/ """

    def __init__(self):

        # any request sent to the API must start with this url
        self.base_url = "https://free.currencyconverterapi.com/api/v6/convert"

    def get_response(self,base_currency,target_currency):

        # example query_sting -> USD_EGP to get exchange rate from Dollar to Egyptian Pound
        url_query_string = base_currency + "_" + target_currency

        request_parameters = {"q": str(url_query_string)}

        try:
            # send a GET request to the API
            currency_converter_request = requests.get(self.base_url , params = request_parameters)

        # show errors to user when request errors occur otherwise, proceed
        except requests.exceptions.RequestException as request_errors:

            print("here")
            print("Opps! something went wrong:")
            print(request_errors)
            return None

        # check if the API is not down
        if currency_converter_request.status_code == requests.codes.ok:

            json_api_response = currency_converter_request.json()

            # check if currency codes are correct

            if json_api_response['query']['count'] == 0:
                print("Opps! something went wrong:")
                print("please check the correctness of currency codes")
                return None

            else:

                modified_response = {"base": base_currency,
                                     "target": target_currency,
                                     "rate": json_api_response['results'][url_query_string]['val'],
                                     "date": str(date.today())
                                    }
                return modified_response
        else:
            return None

import sys
import CurrencyConverterInterface as cci
import json
import DatabaseInterface as dpi
import PrepareDatabase


def egp_exchange_rate():

    if len(sys.argv) > 2 or len(sys.argv) == 1:

        print("Hint! write only the currency code(3 letters) that you want to convert to EGP as an argument ")

    else:

        # create  a database instance
        database_instance = dpi.DatabaseInterface()

        # connect with the fixer interface
        cci_object = cci.CurrencyConverterInterface()

        #store user input (base currency)
        base_currency = sys.argv[1]

        egp_exchange_rate = cci_object .get_response(base_currency=base_currency,target_currency="EGP")

        if egp_exchange_rate is not None:

            print("one " + str(sys.argv[1]) + " equals  " + str(egp_exchange_rate['rate']) + " Egyptian pounds")

            #store currency converter API response in egp_exchange_requests table
            database_instance.insert_record("""INSERT INTO egp_exchange_rates (INFO) VALUES(%s)"""
                                              ,json.dumps(egp_exchange_rate))
        else:
            print("Fix errors and try again ")


if __name__ == "__main__":
    egp_exchange_rate()

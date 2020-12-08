import requests
from skyscannerkey import headers


def get_quote(location_from, location_to, date):

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/" \
          + str(location_from) + "/" + str(location_to) + "/" + str(date)

    response = requests.request("GET", url, headers=headers)

    j = response.json()

    if "Quotes" in j:
        quotes = j["Quotes"]
        carriers = j["Carriers"]

        carrier_dictionary = {}

        for i, carrier in enumerate(carriers):
            carrier_dictionary[carrier["CarrierId"]] = carrier["Name"]

        flight_quotes = []
        for i, quote in enumerate(quotes):
            price = quote["MinPrice"]
            carrier_id = quote["OutboundLeg"]["CarrierIds"][0]
            carrier_name = carrier_dictionary[carrier_id]
            flight_quotes.append('Fly with ' + carrier_name + ' for €' + str(price))

        return flight_quotes
    else:
        return []
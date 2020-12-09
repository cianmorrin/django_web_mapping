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
        places = j["Places"]

        carrier_dictionary = {}

        for i, carrier in enumerate(carriers):
            carrier_dictionary[carrier["CarrierId"]] = carrier["Name"]

        origin_id = ''
        dest_id = ''
        flight_quotes = []
        for i, quote in enumerate(quotes):
            price = quote["MinPrice"]
            carrier_id = quote["OutboundLeg"]["CarrierIds"][0]
            origin_id = quote["OutboundLeg"]["OriginId"]
            dest_id = quote["OutboundLeg"]["DestinationId"]
            carrier_name = carrier_dictionary[carrier_id]
            flight_quotes.append('Fly with ' + carrier_name + ' for €' + str(price))

        pretty_string_start = ''
        pretty_string_end = ''

        for i, place in enumerate(places):
            if place["PlaceId"] == origin_id:
                pretty_string_start = str(place["Name"]) + "(" + str(place["IataCode"]) + ") to "
            elif place["PlaceId"] == dest_id:
                pretty_string_end = str(place["Name"]) + "(" + str(place["IataCode"]) + ") "

        newdate = date[8] + date[9] + "/" + date[5] + date[6] + "/" + date[0] + date[1] + date[2] + date[3]

        if len(pretty_string_start) > 0:
            prettystring = pretty_string_start + pretty_string_end + "on " + newdate
        else:
            prettystring = location_from[:3] + " to " + location_to[:3] + " on " + newdate
        return prettystring, flight_quotes
    else:
        return '', []

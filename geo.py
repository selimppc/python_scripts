import time
from geopy.geocoders import Nominatim
from pprint import pprint

latitude = "23.7935125"
longitude = "90.4254552"


def get_geo():
    """
    :return:
    """
    address = get_address_by_location(latitude, longitude)
    # print all returned data
    pprint(address['address'])
    return "Ok"


def get_address_by_location(latitude, longitude, language="en"):
    """
    :param latitude:
    :param longitude:
    :param language:
    :return:
    """
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        gl = Nominatim(user_agent="rev_geo_coder")
        return gl.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)


if __name__ == "__main__":
    get_geo()

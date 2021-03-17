import requests, json

def locationSnab():
    url = "http://ip-api.com/json/?fields=country,region,regionName,city,zip,lat,lon,timezone,query"
    request = requests.get(url)
    requestMap = json.loads(request.text)
    # requestMap is dict
    #locationInfo = "IP Address: {}\n".format(requestMap["query"]) + "City: {}\n".format(requestMap["city"]) + "Zip code: {}\n".format(str(requestMap["zip"])) + "Region: {}\n".format(requestMap["region"]) + "Country: {}\n".format(requestMap["country"]) + "Timezone: {}\n".format(requestMap["timezone"]) + "Est. Coordinates: {}, {}\n".format(str(requestMap["lat"]), str(requestMap["lon"]))
    locationInfo = "IP address: {0}\nCity: {1}\nZip Code: {2}\nRegion: {3}\nCountry: {4}\nTimezone: {5}\nEst. Coordinates: {6}, {7}".format(requestMap["query"], requestMap["city"], str(requestMap["zip"]), requestMap["region"], requestMap["country"], requestMap["timezone"], str(requestMap["lat"]), str(requestMap["lon"]))
    return locationInfo
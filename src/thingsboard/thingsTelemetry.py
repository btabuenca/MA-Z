class thingsTelemetry:
    """Declare a thingsboard poster object to interact with ThingsBoard platform"""
    def __init__(self, url, relHumidity, envTemperature, soilMoisture, soilWeight, envDaylight, airQuality):
        #Maybe a dict?
        self.url = url
        self.relHumidity = relHumidity
        self.envTemperature = envTemperature
        self.soilMoisture = soilMoisture
        self.soilWeight = soilWeight
        self.envDaylight = envDaylight
        self.airQuality = airQuality

    def __setitem__(self, key, value):
        if key in self.querystring:
            self.querystring[key] = value
            print(self.querystring)
        else:
            print("Error 404: Vulnerability not found")

    def __getitem__(self, item):
        return self.querystring[item]

    querystring = { 
        "relHumidity"   : self.relHumidity,
        "envTemperature": self.envTemperature,
        "soilMoisture"  : self.soilMoisture,
        "soilWeight"    : self.soilWeight,
        "envDaylight"   : self.envDaylight,
        "airQuality"    : self.airQuality
        }

    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    def post(self):
        """POST data to ThingsBoard instance"""
        response = requests.request("POST", self.url, data = json.dumps(self.querystring), headers = self.headers)

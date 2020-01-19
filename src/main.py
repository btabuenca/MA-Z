#Lib imports
import Adafruit_ADS1x15
import spidev
import smbus
import mraa
import time
import requests
import json

#Local imports
from src.i2c import *
from src.gpio import *
from src.thingsboard import *

ENDPOINT = "https://thingsboardinstance.sbc/api/v1/"
TOKEN = "DEVICE TOKEN HERE"
TELEMETRY = "telemetry"

#ETSIAA Team MUST define a logic to execute operations or recolect data.

#poster = thingsTelemetry(ENDPOINT + TOKEN + TELEMETRY)

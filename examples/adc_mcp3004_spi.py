#UPSquared not working correctly on SPI
#Error detected after 3weeks of board testing
import spidev
import time
 
#Define Variables
delay = 2       # May vary
ldr_channel = 0 # May vary by channel connected on ADC
 
#Create SPI bus
spi = spidev.SpiDev()
spi.open(1, 0)
spi.max_speed_hz=1000000
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]  
    return data
 
while True:
    ldr_value = readadc(ldr_channel)
    print("LDR Value: %d" % ldr_value)
    time.sleep(delay)
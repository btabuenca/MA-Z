import time
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance specifying bus number
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=5)

GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} - Peso | {1:>6} - Lluvia | {2:>6} - Tierra1 | {3:>6} - Tierra2 |'.format(*range(4)))
print('-' * 37)

# Main loop for testing puposes
while True:
    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    # Print the ADC values by its corresponding channels.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    # Pause for half a second to let the converter converse.
    time.sleep(0.5)
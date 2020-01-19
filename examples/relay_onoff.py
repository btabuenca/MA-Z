import mraa
import time

#Init testing GPIOs
gpio_1 = mraa.Gpio(13)
gpio_1.dir(mraa.DIR_OUT)


# toggle both gpio's
while True:
    gpio_1.write(1)
    time.sleep(15)
    gpio_1.write(0)
    time.sleep(15)
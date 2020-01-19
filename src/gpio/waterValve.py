import mraa

class waterValve:
        """Declare a water valve object to interact with GPIO relay pin"""
        def __init__(self, gpio):
                self.gpio_1 = mraa.Gpio(gpio)
                self.gpio_1.dir(mraa.DIR_OUT)

        def open(self):
                """Open water valve"""
                self.gpio_1.write(1)

        def close(self):
                """Close water valve"""
                self.gpio_1.write(0)

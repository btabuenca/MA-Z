class ledController:
    """Declare a led controller to light the plant.\nWorks with a RGB led, must be a UV led in prod environment"""
    def __init__(self, gpio1, gpio2, gpio3):
         self.gpio_1 = mraa.Gpio(gpio1)
         self.gpio_2 = mraa.Gpio(gpio2)
         self.gpio_3 = mraa.Gpio(gpio3)
         self.gpio_1.dir(mraa.DIR_OUT)
         self.gpio_2.dir(mraa.DIR_OUT)
         self.gpio_3.dir(mraa.DIR_OUT)

    def on(self,color):
        """Turns ON RGB led with specified color"""
        if color == "rojo":
            self.gpio_1.write(1)
            self.gpio_2.write(0)
            self.gpio_3.write(0)

        if color == "verde":
            self.gpio_1.write(0)
            self.gpio_2.write(1)
            self.gpio_3.write(0)

        if color == "azul":
            self.gpio_1.write(0)
            self.gpio_2.write(0)
            self.gpio_3.write(1)

        if color == "blanco":
            self.gpio_1.write(1)
            self.gpio_2.write(1)
            self.gpio_3.write(1)

    def off(self):
        """Turns OFF RGB led"""
        self.gpio_1.write(0)
        self.gpio_2.write(0)
        self.gpio_3.write(0)
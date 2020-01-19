class adcReader:
    """Declare an adc reader object to interact ADC connected in I2C interface"""
    def __init__(self, adc):
        self.adc = adc
        self.GAIN = 1
        self.soilMoisture = 0
        self.waterLeak = 0
        self.weighCell = 0

    def read(self):
        values = [0]*3

        for i in range(3):
            values[i] = self.adc.read_adc(i, gain=self.GAIN)

        self.soilMoisture = values[0]
        self.waterLeak = values[1]
        self.weighCell = values[2]
class humidityTemp:
    """Declare an humidity and temperature object to interact with I2C SHT85 connected sensor"""
    def __init__(self, bus):
        self.bus = bus
        self.address = 0x44
        self.datablock = 6
        self.temperature = 0
        self.relHumidity = 0

    def read(self):
        """Read relative humidity and temperature of environment"""
        # SHT85 address, 0x44(68)
        self.bus.write_i2c_block_data(self.address, 0x2C, [0x06])

        #Wait to start reading
        #Just for debugging not in production environment
        time.sleep(0.1)

        # SHT85 address, 0x44(68)
        # Read data back from 0x00(00), 6 bytes
        # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
        data = self.bus.read_i2c_block_data(self.address, 0x00, self.datablock)

        # Convert the data
        temp = data[0] * 256 + data[1]
        self.temperature = -45 + (175 * temp / 65535.0)
        self.relHumidity = 100 * (data[3] * 256 + data[4]) / 65535.0
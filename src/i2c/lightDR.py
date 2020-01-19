class lightDR:
    """Declare a light sensor object to interact with I2C LDR connected sensor"""
    def __init__(self, bus):
        self.bus = bus
        self.addr = 0x10
        #Write registers
        als_conf_0 = 0x00
        als_WH = 0x01
        als_WL = 0x02
        pow_sav = 0x03
        #Read registers
        self.als = 0x04
        white = 0x05
        interrupt = 0x06
        # These settings will provide the max range for the sensor (0-120Klx)
        # but at the lowest precision:
        #              LSB   MSB
        confValues = [0x00, 0x13] # 1/8 gain, 25ms IT (Integration Time)
        #Reference data sheet Table 1 for configuration settings
        interrupt_high = [0x00, 0x00] # Clear values
        #Reference data sheet Table 2 for High Threshold
        interrupt_low = [0x00, 0x00] # Clear values
        #Reference data sheet Table 3 for Low Threshold
        power_save_mode = [0x00, 0x00] # Clear values
        #Reference data sheet Table 4 for Power Saving Modes
        self.bus.write_i2c_block_data(self.addr, als_conf_0, confValues)
        self.bus.write_i2c_block_data(self.addr, als_WH, interrupt_high)
        self.bus.write_i2c_block_data(self.addr, als_WL, interrupt_low)
        self.bus.write_i2c_block_data(self.addr, pow_sav, power_save_mode)

    def read(self):
        """Read relative lux level of environment"""
        #The frequency to read the sensor should be set greater than
    	# the integration time (and the power saving delay if set).
        # Reading at a faster frequency will not cause an error, but
        # will result in reading the previous data
        time.sleep(.04) # 40ms
        word = self.bus.read_word_data(self.addr,self.als)
        gain = 1.8432 #Gain for 1/8 gain & 25ms IT
        #Reference www.vishay.com/docs/84323/designingveml7700.pdf
        #Calculating the LUX Level
        val = word * gain
        val = round(val,1) #Round value for presentation
        return val

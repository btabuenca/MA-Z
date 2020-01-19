class airQuality:
    def __init__(self, bus):
        self.iaq = 0
        self.bus = bus
        self.address = 0x5A
        self.datablock = 9
        self.data = 0

    def read(self):
        data = self.bus.read_i2c_block_data(self.address, 0x00, self.datablock)
        #WIP
        # Convert the data
        #if( eco2  !=0 ) *eco2  =  (buf[0]<<8) + (buf[1]<<0);
        
        #if( stat  !=0 ) *stat  =  ( num==IAQCORE_SIZE ? 0 : IAQCORE_STAT_I2CERR ) + (buf[2]<<0); // Add I2C status to chip status
        
        #if( resist!=0 ) *resist=  ((uint32_t)buf[3]<<24) + ((uint32_t)buf[4]<<16) + ((uint32_t)buf[5]<<8) + ((uint32_t)buf[6]<<0); 
        
        #if( etvoc !=0 ) *etvoc =  (buf[7]<<8) + (buf[8]<<0);
        
        # Output data to screen
        #Print values, interpret as datasheet
                    
        #Based on maarten's ESP project
        #https://github.com/maarten-pennings/iAQcore/blob/master/src/iAQcore.cpp

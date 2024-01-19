"""
'Driver' for LabJack U6 with DAC
"""

from u6 import U6
import struct
from device_template import Device


class LabJack(Device):
    DAC_PIN_DEFAULT = 0
    DAC_ADDRESS = 0x12
    EEPROM_ADDRESS = 0x50

    def __init__(self):
        super().__init__('LabJack U6')
        self.device = U6()
        self.dacPin = self.__class__.DAC_PIN_DEFAULT
        self.sclPin = self.dacPin
        self.sdaPin = self.sclPin + 1

        self.device.getCalibrationData()

        self.aSlope = None
        self.aOffset = None
        self.bSlope = None
        self.bOffset = None
        self.get_cal_constants()

    def read_ain(self, pin):
        return self.device.getAIN(pin)

    def write_dac(self, voltage, channel="A"):
        addr = 48
        if channel == "B":
            addr += 1
        self.device.i2c(LabJack.DAC_ADDRESS,
                        [addr, int(((voltage * self.aSlope) + self.aOffset) / 256),
                         int(((voltage * self.aSlope) + self.aOffset) % 256)],
                        SDAPinNum=self.sdaPin, SCLPinNum=self.sclPin)

    def get_cal_constants(self):
        """Loads or reloads the calibration constants for the LJTic-DAC. See datasheet"""
        # make a request
        data = self.device.i2c(LabJack.EEPROM_ADDRESS, [64], NumI2CBytesToReceive=36, SDAPinNum=self.sdaPin,
                               SCLPinNum=self.sclPin)
        response = data['I2CBytes']

        self.aSlope = self.to_double(response[0:8])
        self.aOffset = self.to_double(response[8:16])
        self.bSlope = self.to_double(response[16:24])
        self.bOffset = self.to_double(response[24:32])

    @staticmethod
    def to_double(buffer):
        """
        Name: toDouble(buffer)
        Args: buffer, an array with 8 bytes
        Desc: Converts the 8 byte array into a floating point number.
        """
        right, left = struct.unpack("<Ii", struct.pack("B" * 8, *buffer[0:8]))
        return float(left) + float(right) / (2 ** 32)

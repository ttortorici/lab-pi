"""
'Driver' for Prologix GPIB Controller

author: Teddy Tortorici
"""

import serial
import time


class Prologix:

    SERIAL_PORT = ""
    TIMEOUT = 0.1

    def __init__(self):
        self.id = 'Prologix GPIB Controller'
        # self.gpib_address = gpib_address
        self.port = serial.Serial(self.SERIAL_PORT, 9600, timeout=0.5)

    def attention(self, gpib_address: int) -> None:
        """
        Set the GPIB address for controller to communicate with.
        :param gpib_address: GPIB address to call attention to.
        :return: None
        """
        self.port.write(f"++addr {gpib_address}")

    def read(self) -> str:
        """
        Read from device.
        :return: Message from device.
        """
        self.port.write("++read eoi\n".encode())
        return self.port.read(256)

    def write(self, message: str) -> None:
        """
        Sends a message to device.
        :param message: message to send to device.
        :return: None
        """
        message += "\n"
        self.port.write(message.encode())
        time.sleep(self.__class__.TIMEOUT)

    def query(self, message: str) -> str:
        """
        Query a device by writing to it and then reading from it.
        :param message: message to query with.
        :return: message back from device.
        """
        self.write(message)
        return self.read()

    def idn(self) -> str:
        """
        Query a device for its identification.
        :return: Device self-identification.
        """
        return self.query("*IDN?")

    def rst(self) -> None:
        """
        Reset a device to factory default.
        :return: None
        """
        self.query("*RST")

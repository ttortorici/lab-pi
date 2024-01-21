"""
Server for controlling LabJack U6

author: Teddy Tortorici
"""

from servers.server_template import Server
from devices.prologix import Prologix


class GPIBServer(Server):

    PORT = 23091
    NAME = "GPIB Server"
    device = Prologix()

    def __init__(self):
        super().__init__()
        self.current_addr = None

    def handle(self, message: str) -> str:
        """
        Parse a message of the format
        [addr]::[command]::[message]
        addr - GPIB address for device
        command - R, W, Q
        message - message to send to device
        """
        message = message.split("::")

        # set GPIB address
        if message[0] != self.current_addr:
            self.device.attention(message[0])
            self.current_addr = message[0]

        # read, write, or query
        if message[1] == "R":
            message_out = self.device.read()
        elif message[1] == "W":
            self.device.write(message[2])
            message_out = ""
        elif message[1] == "Q":
            message_out = self.device.query(message[2])

        return message_out

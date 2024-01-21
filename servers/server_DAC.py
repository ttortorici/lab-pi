"""
Server for controlling LabJack U6

author: Teddy Tortorici
"""

from servers.server_template import Server
from devices.labjack import LabJack


class DACServer(Server):

    PORT = 23092
    NAME = "DAC Server"
    device = LabJack()

    def handle(self, message: str) -> str:
        """
        Parse a message of the format
        [command]::[pin]::[volt]
        command - R, W
        pin - a number of a pin
        volt - a voltage to set
        """
        message = message.split("::")
        command = message[0]
        try:
            pin = message[1]
        except IndexError:
            pin = "0"
        try:
            volt = float(message[2])
        except IndexError:
            volt = 0.

        if command == "R":
            message_out = str(self.device.read_ain(int(pin)))
        elif command == "W":
            self.device.write_dac(voltage=volt, channel=pin)
            message_out = f"Set DAC{pin} to {volt} V."
        return message_out

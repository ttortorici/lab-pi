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
            volt = message[2]
        except IndexError:
            volt = "0."

        if command == "R":
            try:
                message_out = str(self.device.read_ain(int(pin)))
            except ValueError:
                print(f"Invalid input for pin. Gave '{pin}', but should be an int")
        elif command == "W":
            if pin not in ["A", "B"]:
                message_out = ""
            else:
                try:
                    self.device.write_dac(voltage=float(volt), channel=pin)
                    message_out = f"Set DAC{pin} to {volt} V."
                except ValueError:
                    print(f"Invalid input for voltage. Gave '{volt}', but should be a float")
        else:
            message_out = ""
        return message_out

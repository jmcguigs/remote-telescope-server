from remote_telescope_server.telescope.serial_telescope import SerialTelescope
from importlib.resources import files
import json


class ZWOAM5(SerialTelescope):
    def __init__(self):
        cmd_file = files("remote_telescope_server.telescope.serial_command_configs").joinpath("zwo_am5.json")
        with open(cmd_file, "r") as f:
            self.cmds = json.load(f)
        print(self.cmds)
        super().__init__(port="/dev/ttyUSB0", baud=self.cmds['PARAMETERS']['BAUD_RATE'], commands=self.cmds)

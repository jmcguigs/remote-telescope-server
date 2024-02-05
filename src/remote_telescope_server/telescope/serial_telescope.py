from remote_telescope_server.telescope.telescope import Telescope
import serial


class SerialTelescope(Telescope):
    def __init__(self, port: str, baud: int, commands: dict):
        self.cmds = commands
        self.port = port
        self.baud = baud
        self.serial = serial.Serial(port, baud)

    def send_command(self, command: str) -> str:
        self.serial.write(command.encode())
        return self.serial.readline().decode()
    
    def slew_to_azel(self, az_deg: float, el: float) -> None:
        command = self.cmds['COMMANDS']['SLEW_AZEL'].format(az_deg, el)
        self.send_command(command)

    def slew_to_radec(self, ra_deg: float, dec_deg: float) -> None:
        command = self.cmds['COMMANDS']['SLEW_RADEC'].format(ra_deg, dec_deg)
        self.send_command(command)

    def sync_to_radec(self, ra_deg: float, dec_deg: float) -> None:
        command = self.cmds['COMMANDS']['SYNC_RADEC'].format(ra_deg, dec_deg)
        self.send_command(command)

    def get_position(self) -> (float, float):
        response = self.send_command(self.cmds['COMMANDS']['GET_POSITION'])
        return tuple(map(float, response.split(',')))
    
    def get_azel(self) -> (float, float):
        response = self.send_command(self.cmds['COMMANDS']['GET_AZEL'])
        return tuple(map(float, response.split(',')))
    
    def get_radec(self) -> (float, float):
        response = self.send_command(self.cmds['COMMANDS']['GET_RADEC'])
        return tuple(map(float, response.split(',')))
    
    def find_home(self) -> None:
        self.send_command(self.cmds['COMMANDS']['FIND_HOME'])


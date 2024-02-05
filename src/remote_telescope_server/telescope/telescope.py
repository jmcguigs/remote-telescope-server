from abc import ABC, abstractmethod


class Telescope(ABC):
    @abstractmethod
    def slew_to_azel(self, az_deg: float, el: float) -> None:
        pass

    @abstractmethod
    def slew_to_radec(self, ra_deg: float, dec_deg: float) -> None:
        pass

    @abstractmethod
    def sync_to_radec(self, ra_deg: float, dec_deg: float) -> None:
        pass

    @abstractmethod
    def get_position(self) -> (float, float):
        pass

    @abstractmethod
    def get_azel(self) -> (float, float):
        pass

    @abstractmethod
    def get_radec(self) -> (float, float):
        pass

    @abstractmethod
    def find_home(self) -> None:
        pass

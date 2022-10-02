from .device import Device
import datetime

class BermadSolenoid(Device):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def on(self) -> bool:
        when: datetime = datetime.datetime.now()
        print(f'Got {self.name}, START watering on {when}')

    def off(self) -> bool:
        when: datetime = datetime.datetime.now()
        print(f'Got {self.name}, STOP watering on {when}')

    def status(self) -> str:
        raise NotImplementedError()
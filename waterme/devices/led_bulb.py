from .device import Device
import datetime

class LEDBulb(Device):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def on(self) -> bool:
        when: datetime = datetime.datetime.now()
        print(f'{self.name}, truned on {when}')

    def off(self) -> bool:
        when: datetime = datetime.datetime.now()
        print(f'{self.name}, truned off {when}')

    def status(self) -> str:
        raise NotImplementedError()
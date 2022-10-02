from abc import ABC
from datetime import datetime

class Device(ABC):
    def on(self, when: datetime) -> bool:
        raise NotImplementedError()

    def off(self, when: datetime) -> bool:
        raise NotImplementedError()

    def status(self) -> str:
        raise NotImplementedError()
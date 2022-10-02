"""
Rasppberi PI that will hold to mapping of GPIO to devices according to their registretion
"""

from waterme.devices.device import Device


class Controller:
    device_mapper: dict[str, Device] = {}
    devices_currently_working: set = set()

    def __init__(self) -> None:
        # setup
        pass

    def connect(self) -> bool:
        pass
    
    def status(self) -> None:
        print(f'currenlly working devices({len(self.devices_currently_working)}): {self.devices_currently_working}')

    def register_device(self, device_instance: Device) -> None:
        if device_instance.name not in Controller.device_mapper:
            Controller.device_mapper[device_instance.name] = device_instance

    def water(self, name) -> None:
        device = self.device_mapper.get(name)
        device.on()
        self.devices_currently_working.add(device.name)
        print(f'Device {device.name} was turned on')

    def stop_water(self, name) -> None:
        device = self.device_mapper.get(name)
        device.off()
        self.devices_currently_working.remove(device.name)
        print(f'Device {device.name} was turned off')

    def water_all(self) -> None:
        for device_name in self.device_mapper:
             self.water(device_name)

    def stop_water_all(self) -> None:
        for device_name in self.device_mapper:
            self.stop_water(device_name)
    
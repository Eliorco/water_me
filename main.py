from waterme.devices.led_bulb import LEDBulb
from waterme.devices.bermad_solenoid import BermadSolenoid
from waterme.controller import Controller
from time import sleep


def main():
    # A short demo for registering devices and turnning them on and off
    controller = Controller()
    valv1 = BermadSolenoid('BermadSolenoid1')
    valv2 = BermadSolenoid('BermadSolenoid2')
    led1 = LEDBulb('BigAssLED')
    controller.register_device(valv1)
    controller.register_device(valv2)
    controller.register_device(led1)

    try:
        while True:
            controller.water_all()
            sleep(0.5)
            controller.status()
            controller.stop_water_all()
            sleep(0.2)
            controller.status()
            controller.water('BermadSolenoid2')
            controller.water('BigAssLED')
            sleep(0.5)
            controller.status()
            controller.water('BermadSolenoid1')
            controller.stop_water('BermadSolenoid1')
            sleep(0.5)
            controller.status()

            controller.stop_water('BermadSolenoid2')
            controller.status()
    except KeyboardInterrupt:
        print('\nClosing program')

if __name__ == '__main__':
    main()
    # flask server api
    # cellery worker for a/sync jobs + redis broker
    # db - postgress -> plants, watering log, aggregated data
    # dashboard will be part of flask for now
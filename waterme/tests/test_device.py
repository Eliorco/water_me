import unittest
from devices.bermad_solenoid import BermadSolenoid
from devices.led_bulb import LEDBulb 

class TestDevice(unittest.TestSuite):

    def test_devuce_sanity(self):
        # Arrange
        # Act
        device_list = [BermadSolenoid(), LEDBulb()]
        # Assert
        self.assertTrue(all(d.on() for d in device_list))

if __name__ == '__main__':
    unittest.main()
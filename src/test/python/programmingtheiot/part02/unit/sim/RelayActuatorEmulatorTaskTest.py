####
# Unit test for RelayActuatorEmulatorTask
#
import unittest
from programmingtheiot.cda.emulated.RelayActuatorEmulatorTask import RelayActuatorEmulatorTask
import programmingtheiot.common.ConfigConst as ConfigConst

class RelayActuatorEmulatorTaskTest(unittest.TestCase):
    def setUp(self):
        self.actuator = RelayActuatorEmulatorTask()

    def test_activate_on(self):
        data = self.actuator.activate(ConfigConst.COMMAND_ON)
        self.assertIsNotNone(data)
        self.assertEqual(data.getCommand(), ConfigConst.COMMAND_ON)
        self.assertEqual(data.getValue(), 1.0)

    def test_activate_off(self):
        data = self.actuator.activate(ConfigConst.COMMAND_OFF)
        self.assertIsNotNone(data)
        self.assertEqual(data.getCommand(), ConfigConst.COMMAND_OFF)
        self.assertEqual(data.getValue(), 0.0)

if __name__ == "__main__":
    unittest.main()

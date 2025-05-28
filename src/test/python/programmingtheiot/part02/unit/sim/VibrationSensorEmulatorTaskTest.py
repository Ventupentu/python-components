####
# Unit test for VibrationSensorEmulatorTask
#
import unittest
from programmingtheiot.cda.emulated.VibrationSensorEmulatorTask import VibrationSensorEmulatorTask

class VibrationSensorEmulatorTaskTest(unittest.TestCase):
    def setUp(self):
        self.sensor = VibrationSensorEmulatorTask()

    def test_generateTelemetry(self):
        data = self.sensor.generateTelemetry()
        self.assertIsNotNone(data)
        self.assertGreaterEqual(data.getValue(), 0.0)
        self.assertLessEqual(data.getValue(), 1.0)

    def test_isAbnormal(self):
        self.assertFalse(self.sensor.isAbnormal(0.5))
        self.assertTrue(self.sensor.isAbnormal(0.8))

if __name__ == "__main__":
    unittest.main()

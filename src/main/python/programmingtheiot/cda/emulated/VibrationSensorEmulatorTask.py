#####
# 
# This class implements a vibration sensor emulator for the Programming the Internet of Things project.
#
# It is designed to be integrated similarly to the humidity and temperature sensor emulators.
#

from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
import random

class VibrationSensorEmulatorTask(BaseSensorSimTask):
	"""
	Emulates a vibration sensor (e.g., SW-420 or MPU6050).
	"""

	def __init__(self):
		super(VibrationSensorEmulatorTask, self).__init__(
			name = 'VibrationSensor',
			typeID = 1020 # Custom type ID for vibration sensor
		)
		self.threshold = 0.7  # Example threshold for abnormal vibration

	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(name = self.getName(), typeID = self.getTypeID())
		# Simulate vibration value (0.0 = no vibration, 1.0 = max)
		vibration = random.uniform(0.0, 1.0)
		sensorData.setValue(vibration)
		self.latestSensorData = sensorData
		return sensorData

	def isAbnormal(self, value: float) -> bool:
		"""Returns True if vibration is above threshold."""
		return value > self.threshold

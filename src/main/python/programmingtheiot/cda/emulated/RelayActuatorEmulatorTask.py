#####
# 
# This class implements a relay actuator emulator for anti-damage response.
#
# It is designed to be integrated similarly to other actuators.
#

from programmingtheiot.data.ActuatorData import ActuatorData
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

class RelayActuatorEmulatorTask(BaseActuatorSimTask):
	"""
	Emulates a relay actuator for disconnecting or reducing speed of equipment.
	"""

	def __init__(self):
		super(RelayActuatorEmulatorTask, self).__init__(
			name = 'RelayActuator',
			typeID = 2002 # Custom type ID for relay actuator
		)
		self.isOn = False

	def activate(self, command: int) -> ActuatorData:
		actuatorData = ActuatorData(name = self.getName(), typeID = self.getTypeID())
		if command == ConfigConst.COMMAND_ON:
			self.isOn = True
		elif command == ConfigConst.COMMAND_OFF:
			self.isOn = False
		actuatorData.setCommand(command)
		actuatorData.setValue(1.0 if self.isOn else 0.0)
		return actuatorData

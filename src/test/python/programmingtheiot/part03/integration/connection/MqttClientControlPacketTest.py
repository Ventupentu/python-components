import logging
import unittest
from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.DataUtil import DataUtil


class MqttClientControlPacketTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(
            format='%(asctime)s:%(module)s:%(levelname)s:%(message)s',
            level=logging.DEBUG
        )
        logging.info("Ejecutando MqttClientControlPacketTest...")
        cls.cfg = ConfigUtil()
        cls.mcc = MqttClientConnector(clientID="TestClientControlPacket")

    def testConnectAndDisconnect(self):
        logging.info("---- TEST CONNECT / DISCONNECT ----")
        result = self.mcc.connectClient()
        self.assertTrue(result, "No se pudo conectar al broker MQTT.")
        sleep(1)
        result = self.mcc.disconnectClient()
        self.assertTrue(result, "No se pudo desconectar del broker MQTT.")

    def testPing(self):
        logging.info("---- TEST PINGREQ / PINGRESP ----")
        self.mcc.connectClient()
        keep_alive = self.mcc.keepAlive
        logging.info(f"Esperando {keep_alive + 2} segundos para forzar PINGREQ...")
        sleep(keep_alive + 2)
        self.mcc.disconnectClient()

    def testPublishQoS1And2(self):
        logging.info("---- TEST PUBLISH / PUBACK / PUBREC / PUBREL / PUBCOMP ----")
        self.mcc.connectClient()
        resource = ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE

        # Crear mensaje de prueba
        data = ActuatorData()
        data.setCommand(ConfigConst.COMMAND_ON)
        data.setValue(22.0)
        payload = DataUtil().actuatorDataToJson(data)

        # QoS 1 -> genera PUBLISH + PUBACK
        logging.info("Publicando mensaje con QoS 1")
        result_qos1 = self.mcc.publishMessage(resource, payload, qos=1)
        self.assertTrue(result_qos1)
        sleep(2)

        # QoS 2 -> genera PUBLISH + PUBREC + PUBREL + PUBCOMP
        logging.info("Publicando mensaje con QoS 2")
        result_qos2 = self.mcc.publishMessage(resource, payload, qos=2)
        self.assertTrue(result_qos2)
        sleep(2)

        self.mcc.disconnectClient()

    def testSubscribeUnsubscribe(self):
        logging.info("---- TEST SUBSCRIBE / SUBACK / UNSUBSCRIBE / UNSUBACK ----")
        self.mcc.connectClient()
        resource = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE

        result_sub = self.mcc.subscribeToTopic(resource, qos=1)
        self.assertTrue(result_sub)
        sleep(2)

        result_unsub = self.mcc.unsubscribeFromTopic(resource)
        self.assertTrue(result_unsub)
        sleep(1)

        self.mcc.disconnectClient()


if __name__ == '__main__':
    unittest.main()

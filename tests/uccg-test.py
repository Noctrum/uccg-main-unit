'''Tu będą testy'''

import sys
sys.path.append('../uccg-main-unit')
import main
import unittest
import sensors

class TestStringMethods(unittest.TestCase):

    def test_init(self):
        self.assertTrue(main.init)
    def test_temp(self):
        tempSensor = sensors.TemperatureSensor("TempSensor", 2)
        tempSensor.value = list(range(0, 50))
        self.assertEqual(tempSensor.read(), list(range(0, 50)))
        self.assertEqual(tempSensor.read("C"), list(range(0, 50)))
        self.assertEqual(tempSensor.read("K"), list(range(273, 273+50)))
        self.assertEqual(tempSensor.read("C"), list(range(0, 50)))
        self.assertEqual(tempSensor.read("F"), list([i*1.8+32 for i in range(0, 50)]))


if __name__ == '__main__':
    unittest.main()

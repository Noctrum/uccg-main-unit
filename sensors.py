"""! @brief Defines the sensor classes."""
##
# @file sensors.py
#
# @brief Defines the sensor classes.
#
# @section description_sensors Description
# Defines the base and end user classes for various sensors.
# - Sensor (base class)
# - TemperatureSensor
# - MoistureSensor
#
# @section libraries_sensors Imported Libraries/Modules
# - random (https://docs.python.org/3/library/random.html)
#   - randint function
# - adafruit-circuitpython-mcp3xxx (https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx/)
#   - AnalogIn and mcp3008 classes
# - busio (https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html)
#   - SPI class
# - digitalio (https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html)
#   - DigitalInOut class
# - board (https://docs.circuitpython.org/en/latest/shared-bindings/board/index.html)
#   - Board specific pin names
#
# @section author_sensors Author(s)
# - Created by Damian Dompke on 26/05/2022.
# - Modified by Dawid Lentka on 31/05/2022.
#
# Copyright (c) 2022 Grupa Dompke-Lentka-Świrydczuk.  All rights reserved.


#Imports
import random
# # from adafruit_mcp3xxx.analog_in import AnalogIn
# import adafruit_mcp3xxx.mcp3008 as MCP
# import busio
# import digitalio
# import board


class Sensor:
    """! The sensor base class.
    Defines the base class utilized by all sensors.
    """
    def __init__(self, name, pin):
        """! The Sensor base class initializer.
        @param name  The name of the sensor.
        @param pin  The pin number of the sensor.
        @return  An instance of the Sensor class initialized with the specified name.
        """
        ## The name of the sensor.
        self.name = name
        self.pin = pin
        ## The value of the sensor.
        self.value = random.choices(range(0, 50), k=10000)
    def read(self):
        """! Gets current value from the sensor.
        @return Measured value
        """
        return self.value

class TemperatureSensor(Sensor):
    """! The temperature sensor class.
    Provides access to the connected temperature sensor.
    """

    def __init__(self, name, pin):
        """! The TemperatureSensor class initializer.
        @param name  The name of the temperature sensor.
        @param pin  The pin number of the temperature sensor.
        @return  An instance of the TemperatureSensor class initialized with the specified name, pin number and unit.
        """
        super().__init__(name, pin)
        self.tempUnit = "C"
    def kelvin2Celsius(self):
        """! Converts the temperature from Kelvin to celsius.
        """
        self.value = [i - 273 for i in self.value]
    def kelvin(self):
        """! Converts the temperature to Kelvin.
        """
        self.value = [i + 273 for i in self.value]

    def fahrenheit(self):
        """! Converts the temperature to Fahrenheit.
        """
        self.value = [i * 1.8 + 32 for i in self.value]
    def fahrenheit2Celsius(self):
        """! Converts the temperature from Fahrenheit to celsius.
        """
        self.value = [(i-32)/ 1.8 for i in self.value]
    def set_temp_scale(self, unit="C"):
        """! Sets temperature unit and converts temp.
        @param unit  The target temperature unit: "K" (Kelvin), "F" (Fahrenheit) and "C" (Celsius)
            defaults to Celsius if no valid value provided.
        """
        if unit != self.tempUnit:
            if self.tempUnit == "C":
                if unit == "F":
                    self.fahrenheit()
                    self.tempUnit = "F"
                if unit == "K":
                    self.kelvin()
                    self.tempUnit = "K"
            else:
                if self.tempUnit == "F":
                    self.fahrenheit2Celsius()
                if self.tempUnit == "K":
                    self.kelvin2Celsius()
                self.tempUnit = "C"
                self.set_temp_scale(unit)



    def read(self):
        """! Gets current temperature reading and returns it.
        @return Measured temperature in selected unit.
        """
        return self.value


class MoistureSensor(Sensor):
    """! The moisture sensor class.
    Provides access to the connected moisture sensor.
    """

    def __init__(self, name, pin):
        """! The MoistureSensor class initializer.
        @param name  The name of the moisture sensor.
        @param pin  The pin number of the moisture sensor.
        @return  An instance of the MoistureSensor class initialized with the specified name and unit.
        """
        super().__init__(name, pin)
   
    def read(self):
        """! Gets current moisture reading and returns it.
        @return Measured moisture.
        """

#!/usr/bin/env python3
"""! @brief uClimate Control Greenhouse documentation."""
##
# @mainpage uCCG
#
# @section description_main Description
# uCCG is a system for controling and monitoring climate conditions in an automated Greenhouse.
#
# @section notes_main Notes
# - This documentation is mostly placeholder.
# - Seriously, don't use this.
#
# Copyright (c) 2022 Grupa Dompke-Lentka-Świrydczuk.  All rights reserved.
##
# @file main.py
#
# @brief Example Python program with Doxygen style comments.
#
# @section description_main Description
# Example Python program with Doxygen style comments.
#
# @section libraries_main Imported Libraries/Modules
# - time standard library (https://docs.python.org/3/library/time.html)
#   - Access to sleep function.
# - sensors module (local)
#   - Access to Sensor and TemperatureSensor classes.
#
# @section notes_main Notes
# - Comments are Doxygen compatible.
#
# @section todo_main TODO
# - Implement everything.
#   - Make more bullet lists in documentation,
#     - ...and make them deeeeper.
#
# @section author_main Author(s)
# - Created by Damian Dompke on 26/05/2022.
# - Modified by Dawid Lentka on 31/05/2022.
#
# Copyright (c) 2022 Grupa Dompke-Lentka-Świrydczuk.  All rights reserved.


# Imports
from time import sleep
import sensors


# Global Constants
## The mode of operation; 0 = normal, 1 = debug.
DEBUG = 1


# Functions
def init():
    """! Initializes the program."""
    if DEBUG:
        print("Initializing program.")

def send_report():
    """! Sends a report to the server."""
    print("Hello world")

def main():
    """! Main program entry."""
    init()  # program initialization
    # Sensors
    sensor = sensors.Sensor("MySensor")
    print(sensor.read())
    
if __name__ == "__main__":
    main()
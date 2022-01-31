from pyvisa.resources import MessageBasedResource
from enum import Enum


class Sense:
    def __init__(self, dmm: MessageBasedResource):
        self._dmm = dmm

    def function(self, function):
        """ Send command that selects the active measure function.

        Set this command to the type of measurement you want to make. Reading this command returns the
        measure function that is presently active. If you send this query when a digitize measurement
        function is selected, this returns NONE. If a channel is closed when you assign a function to
        the channel, all other channels are opened.

        Parameters
        ----------
        function : Function
            Function to activate
        """
        self._dmm.write(f":SENS:FUNC \"{function.value}\"")

    def range(self, function, range):
        """ Send command that selects the positive full-scale measure range.

        You can assign any real number using this command. The instrument selects the closest fixed range that
        is large enough to measure the entered number. For example, for current measurements, if you expect a
        reading of approximately 9 mA, set the range to 9 mA to select the 10 mA range. When you read this setting,
        you see the positive full-scale value of the measurement range that the instrument is presently using. This
        command is primarily intended to eliminate the time that is required by the instrument to automatically
        search for a range. When a range is fixed, any signal greater than the entered range generates an overrange
        condition. When an overrange condition occurs, the front panel displays "Overflow" and the remote interface
        returns 9.9e+37.

        When you set a value for the measurement range, the measurement autorange setting is automatically disabled
        for the selected measurement function (if supported by that function). The range for measure functions
        defaults to autorange for all measure functions. If you switch from a fixed range to autorange, autorange
        is set to off. The range remains at the fixed range until a measurement is made, at which time the range is
        set to accommodate the new measurement.

        Parameters
        ----------
        function : Function
            Function to which the setting applies
        range : Range
            Range to set for the selected function
        """
        self._dmm.write(f":SENS:{function.value}:RANG {range.value}")


class Function(Enum):
    VOLTAGE_DC = "VOLT:DC"
    VOLTAGE_AC = "VOLT:AC"
    CURRENT_DC = "CURR:DC"
    CURRENT_AC = "CURR:AC"
    RESISTANCE = "RES"
    DIODE = "DIOD"
    CAPACITANCE = "CAP"
    TEMPERATURE = "TEMP"
    CONTINUITY = "CONT"

class Range(Enum):
    VOLTAGE_DC_100mV = "100e-3"
    VOLTAGE_DC_1V = "1"
    VOLTAGE_DC_10V = "10"
    VOLTAGE_DC_100V = "100"
    CURRENT_DC_10uA = "10e-6"
    CURRENT_DC_100uA = "100e-6"
    CURRENT_DC_1mA = "1e-3"
    CURRENT_DC_10mA = "10e-3"
    CURRENT_DC_100mA = "100e-3"
    CURRENT_DC_1A = "1"
    CURRENT_DC_3A = "3"

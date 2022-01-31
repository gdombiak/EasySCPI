from pyvisa.resources import MessageBasedResource


class Output:
    def __init__(self, dp832: MessageBasedResource):
        self._dp832 = dp832

    def turn_on(self, channel: int, on: bool):
        """ Send command to enable or disable the output of the specified channel.

        Make sure that the current setting will not affect the device connected to the
        power supply before enabling the channel output.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        on: bool
            True to turn the channel on
        """
        state = 'ON' if on else 'OFF'
        self._dp832.write(f':OUTP:STAT CH{channel},{state}')

    def query_mode(self, channel: int) -> str:
        """ Send command that queries the current output mode of the specified channel.

        DP800 series power supply provides three output modes, including CV (Constant Voltage),
        CC (Constant Current) and UR (Unregulated). In CV mode, the output voltage equals the voltage
        setting value and the output current is determined by the load; in CC mode, the output current
        equals the current setting value and the output voltage is determined by the load; UR is the
        critical mode between CV and CC modes.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        Returns
        -------
        str
            Current output mode of the specified channel.
        """
        return self._dp832.query(f':OUTP:MODE? CH{channel}')

    def overcurrent_protection(self, channel: int, on: bool):
        """ Send command to enable or disable the overcurrent protection (OCP) function of the specified channel.

        When the overcurrent protection function is enabled, the output will turn off automatically when the
        output current exceeds the overcurrent protection value currently set (:OUTPut:OCP:VALue). You can send
        the :OUTPut:OCP:ALAR? or :OUTPut:OCP:QUES? command to query whether overcurrent protection occurred on
        the specified channel currently.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        on: bool
            True to turn overcurrent protection on
        """
        state = 'ON' if on else 'OFF'
        self._dp832.write(f':OUTP:OCP CH{channel},{state}')

    def query_overcurrent_protection(self, channel: int) -> bool:
        """ Send command that queries the status of the overcurrent protection (OCP) function of the specified channel.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        Returns
        -------
        bool
            True if overcurrent protection is enabled
        """
        return self._dp832.query(f':OUTP:OCP? CH{channel}') == "ON"

    def overcurrent_protection_value(self, channel: int, value: float):
        """ Send command to set the overcurrent protection value of the specified channel.

        When the overcurrent protection function is enabled, the output will turn off automatically when the
        output current exceeds the overcurrent protection value currently set (:OUTPut:OCP:VALue). You can send
        the :OUTPut:OCP:ALAR? or :OUTPut:OCP:QUES? command to query whether overcurrent protection occurred on
        the specified channel currently.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        value: float
            Value to set
        """
        self._dp832.write(f':OUTP:OCP:VAL CH{channel},{value}')

    def overvoltage_protection(self, channel: int, on: bool):
        """ Send command to enable or disable the overvoltage protection (OVP) function of the specified channel.

        When the overvoltage protection function is enabled, the output will turn off automatically when the output
        voltage exceeds the overvoltage protection value currently set (:OUTPut:OVP:VALue). You can send
        the :OUTPut:OVP:ALAR? or :OUTPut:OVP:QUES? command to query whether overvoltage protection occurred on
        the specified channel currently.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        on: bool
            True to turn overvoltage protection on
        """
        state = 'ON' if on else 'OFF'
        self._dp832.write(f':OUTP:OVP CH{channel},{state}')

    def query_overvoltage_protection(self, channel: int) -> bool:
        """ Send command that queries the overvoltage protection (OVP) function of the specified channel.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        Returns
        -------
        bool
            True if overvoltage protection is enabled
        """
        return self._dp832.query(f':OUTP:OVP? CH{channel}') == "ON"

    def overvoltage_protection_value(self, channel: int, value: float):
        """ Send command to set the overvoltage protection (OVP) value of the specified channel.

        When the overvoltage protection function is enabled, the output will turn off automatically when the output
        voltage exceeds the overvoltage protection value currently set (:OUTPut:OVP:VALue). You can send
        the :OUTPut:OVP:ALAR? or :OUTPut:OVP:QUES? command to query whether overvoltage protection occurred on
        the specified channel currently.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        value: float
            Value to set
        """
        self._dp832.write(f':OUTP:OVP:VAL CH{channel},{value}')


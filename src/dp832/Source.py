from pyvisa.resources import MessageBasedResource


class Source:
    def __init__(self, dp832: MessageBasedResource):
        self._dp832 = dp832

    def current(self, channel: int, value: float):
        """ Send command to set the current of the specified channel.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        value : float
            Value to set
        """
        self._dp832.write(f':SOUR{channel}:CURR {value}')

    def voltage(self, channel: int, value: float):
        """ Send command to set the voltage of the specified channel.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        value : float
            Value to set
        """
        self._dp832.write(f':SOUR{channel}:VOLT {value}')



from pyvisa.resources import MessageBasedResource


class Instrument:
    def __init__(self, dp832: MessageBasedResource):
        self._dp832 = dp832

    def nselect(self, channel: int):
        """ Send command to select the current channel.

        Parameters
        ----------
        channel : int
            The parameters 1, 2 and 3 represent CH1, CH2 and CH3 respectively.
        """
        self._dp832.write(f':INST:NSEL {channel}')

    def query_nselect(self) -> int:
        """ Send command that queries the current channel

        Returns
        -------
        int
            Current channel in numeric form.
        """
        return int(self._dp832.query(':INST:NSEL?'))

    def select(self, channel: str):
        """ Send command to select the current channel.

        Parameters
        ----------
        channel : str
            Channel CH1, CH2 or CH3.
        """
        self._dp832.write(f':INST:SELE {channel}')

    def query_select(self) -> str:
        """ Send command that queries the current channel

        Returns
        -------
        str
            Current channel in text form.
        """
        return self._dp832.query(':INST:SELE?')

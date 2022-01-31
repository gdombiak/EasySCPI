from pyvisa.resources import MessageBasedResource


class Timer:
    def __init__(self, dp832: MessageBasedResource):
        self._dp832 = dp832

    def cycles(self, number: int):
        """ Send command to set the number of cycles of the timer.

        The number of cycles is defined as the number of times that the instrument performs timing output
        according to the preset voltage/current. You can set the number of cycles to infinite (I) or a
        specified value (N,<value>).

        The total number of groups in timing output = the number of groups × the number of cycles; wherein, the
        number of groups is set by the :TIMEr:GROUPs command.

        The power supply will terminate the timer function when the total number of groups of outputs is
        finished. At this point, the state of the power supply depends on the setting of the :TIMEr:ENDState command.

        Parameters
        ----------
        number : int
            Number of cycles of the timer
        """
        self._dp832.write(f':TIME:CYCLE N,{number}')

    def query_cycles(self) -> int:
        return int(self._dp832.query(':TIME:CYCLE?'))

    def groups(self, number):
        self._dp832.write(f':TIME:GROUP {number}')

    def query_groups(self) -> int:
        return int(self._dp832.query(':TIME:GROUP?'))

    def parameter(self, group, voltage, current, seconds):
        """
        Set the timer parameters of the specified group

        Parameters
        ----------
         group : int
            Number of group. Starts at 0
        voltage: float
            The voltage range of the current channel
        current: float
            The current range of the current channel. In AMPS
        seconds: int
            Number of seconds this setting will be applied
        """
        self._dp832.write(f':TIME:PARA {group},{voltage},{current},{seconds}')

    def turn_off_when_done(self, off: bool):
        state = 'OFF' if off else 'LAST'
        self._dp832.write(f':TIME:ENDS {state}')

    def turn_on(self, on: bool):
        """
        Enable or disable the timing output function. Before enabling timer
        you have to first select a channel. Timer will run on selected
        channel.

        Parameters
        ----------
         on : bool
            True if timer will be enabled
        """
        state = 'ON' if on else 'OFF'
        self._dp832.write(f':TIME:STAT {state}')

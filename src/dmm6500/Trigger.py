from pyvisa.resources import MessageBasedResource


class Trigger:
    def __init__(self, dmm: MessageBasedResource):
        self._dmm = dmm

    def duration_loop(self, duration: int, delay: int, buffer: str):
        """ Send command that loads a trigger-model template configuration that makes continuous measurements
        for a specified amount of time.

        When you load this trigger-model template, you can specify amount of time to make a measurement and the
        length of the delay before the measurement. The rear-panel EXTERNAL TRIGGER OUT terminal is asserted at
        the end of each measurement. After selecting a trigger-model template, you can view the trigger-model
        blocks in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure.
        You can also add or delete blocks and change trigger model settings from this screen. You can use the
        TRIGger:BLOCk:LIST? command to view the trigger-model blocks in a list format.

        Parameters
        ----------
        duration : int
            The amount of time for which to make measurements in seconds (500 ns to 100 ks)
        delay : int
            The delay time before each measurement in seconds (167 ns to 10 ks); default is 0 for no delay
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        """
        self._dmm.write(f"TRIG:LOAD \"DurationLoop\", {duration}, {delay}, \"{buffer}\"")

    def simple_loop(self, count: int, delay: int, buffer: str):
        """ Send command that loads a trigger-model template configuration.

        This command sets up a loop that sets a delay, makes a measurement, and then repeats the loop the number
        of times you define in the Count parameter. The rear-panel EXTERNAL TRIGGER OUT terminal is asserted at
        the end of each measurement. After selecting a trigger-model template, you can view the trigger-model blocks
        in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure. You can
        also add or delete blocks and change trigger model settings from this screen. You can use the
        TRIGger:BLOCk:LIST? command to view the trigger-model blocks in a list format.

        Parameters
        ----------
        count : int
            The number of measurements the instrument will make
        delay : int
            The delay time before each measurement in seconds (167 ns to 10 ks); default is 0 for no delay
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        """
        self._dmm.write(f"TRIG:LOAD \"SimpleLoop\", {count}, {delay}, \"{buffer}\"")

    def empty(self):
        """ Send command that resets the trigger model.

        When you load this trigger-model template, any blocks that have been defined in the trigger model are
        cleared so the trigger model has no blocks defined.
        """
        self._dmm.write(f"TRIG:LOAD \"Empty\"")

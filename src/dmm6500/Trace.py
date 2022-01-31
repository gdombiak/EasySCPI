from pyvisa.resources import MessageBasedResource
from enum import Enum


class Trace:
    def __init__(self, dmm: MessageBasedResource):
        self._dmm = dmm

    def actual(self, buffer: str) -> int:
        """ Send command that retrieves the number of readings in the specified reading buffer.

        Parameters
        ----------
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        Returns
        -------
        int
            Number of readings in the specified reading buffer.
        """
        return int(self._dmm.query(f":TRACe:ACTual? \"{buffer}\""))

    def data(self, end_index: int, buffer: str, element) -> str:
        """ Send command that retrieves specified data elements from a specified reading buffer.

        The output of :TRACe:DATA? is affected by the data format selected by :FORMat[:DATA]. If you set
        FORMat[:DATA] to REAL or SREAL, you will have fewer options for buffer elements. The only buffer
        elements available are READing, RELative, and EXTRa. If you request a buffer element that is not
        permitted for the selected data format, the instrument generates the error 1133, "Parameter 4,
        Syntax error, expected valid name parameters."

        Parameters
        ----------
        end_index : int
            Ending index of the buffer to return
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        element : Element
            Element in the buffer to print
        Returns
        -------
        int
            Data elements from a specified reading buffer.
        """
        return self._dmm.query(f":TRACe:DATA? 1, {end_index}, \"{buffer}\", {element.value}")

    def make(self, buffer: str, size: int):
        """ Send command that creates a user-defined reading buffer.

        The buffer name for a user-defined reading buffer cannot be defbuffer1 or defbuffer2. In addition,
        the buffer name must not already exist as a global variable, a local variable, table, or array. If you
        create a reading buffer that has the same name as an existing user-defined buffer, the event message 1115,
        "Parameter error: TRACe:MAKE cannot take an existing reading buffer name" is generated. When you create a
        reading buffer, it becomes the active buffer. If you create two reading buffers, the last one you create
        becomes the active buffer.

        If you select 0, the instrument creates the largest reading buffer possible based on the available memory
        when the buffer is created. The default fill mode of a user-defined buffer is once. You can change it to
        continuous later. Once the buffer style is selected, it cannot be changed. Not all remote commands are
        compatible with the writable and full writable buffer styles. Check the Details section of the command
        descriptions before using them with any of these buffer styles. Writable reading buffers are used to
        bring external data into the instrument. You cannot assign them to collect data from the instrument. You
        can change the buffer capacity for an existing buffer through the front panel or by using the
        :TRACe:POINts command.

        Parameters
        ----------
        buffer : str
            A user-supplied string that indicates the name of the buffer
        size : int
            A number that indicates the maximum number of readings that can be stored in <bufferName>;
            minimum is 10; set to 0 to maximize the buffer size
        """
        return self._dmm.write(f":TRACe:MAKE \"{buffer}\", {size}")

    def delete(self, buffer: str):
        """ Send command that deletes a user-defined reading buffer.

        You cannot delete the default reading buffers, defbuffer1 and defbuffer2.

        Parameters
        ----------
        buffer : str
            A string that contains the name of the user-defined reading buffer to delete
        """
        return self._dmm.write(f":TRACe:DEL \"{buffer}\"")

    def stats_clear(self, buffer: str):
        """ Send command to clear all readings and statistics from the specified buffer.

        Parameters
        ----------
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        """
        self._dmm.write(f":TRAC:STAT:CLE \"{buffer}\"")

    def stats_average(self, buffer: str) -> float:
        """ Send command that retrieves the average of all readings in the buffer.

        This command returns the average reading calculated from all the readings in the specified reading buffer.
        When the reading buffer is configured to fill continuously and overwrite old data with new data, the
        buffer statistics include the data that was overwritten. To get statistics that do not include data that
        has been overwritten, define a large buffer size that will accommodate the number of readings you will make.

        Parameters
        ----------
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        Returns
        -------
        float
            Average of all readings in the buffer.
        """
        return float(self._dmm.query(f":TRAC:STAT:AVER? \"{buffer}\""))

    def stats_max(self, buffer: str) -> float:
        """ Send command that retrieves the maximum reading value in the reading buffer.

        Parameters
        ----------
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        Returns
        -------
        float
            Maximum reading value in the reading buffer.
        """
        return float(self._dmm.query(f":TRAC:STAT:MAX? \"{buffer}\""))

    def stats_min(self, buffer: str) -> float:
        """ Send command that retrieves the minimum reading value in the reading buffer.

        Parameters
        ----------
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        Returns
        -------
        float
            Minimum reading value in the reading buffer.
        """
        return float(self._dmm.query(f":TRAC:STAT:MIN? \"{buffer}\""))

    def stats_peak_to_peak(self, buffer: str) -> float:
        """ Send command that retrieves the peak-to-peak value of all readings in the reading buffer.

        Parameters
        ----------
        buffer : str
            A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the
            name of a user-defined buffer
        Returns
        -------
        float
            Peak-to-peak value of all readings in the reading buffer.
        """
        return float(self._dmm.query(f":TRAC:STAT:PK2Pk? \"{buffer}\""))


class Element(Enum):
    FORMATTED = "FORM"  # The measured value as it appears on the front panel
    READING = "READ"  # The measurement reading
    RELATIVE = "REL"  # The relative time when the data point was measured
    TIMESTAMP = "TST"  # The timestamp when the data point was measured

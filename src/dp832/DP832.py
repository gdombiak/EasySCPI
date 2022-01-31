from pyvisa import ResourceManager
from pyvisa.resources import MessageBasedResource

from dp832.Instrument import Instrument
from dp832.Output import Output
from dp832.Source import Source
from dp832.Timer import Timer


class DP832:
    def __init__(self, resource_manager: ResourceManager) -> None:
        super().__init__()
        self._resourceManager = resource_manager
        self._dp832 = None
        self.instrument: Instrument = None
        self.output: Output = None
        self.timer: Timer = None
        self.source: Source = None

    def open(self, resource_name: str):
        """ Return an instrument for the resource name. A session will be created.

        Parameters
        ----------
        resource_name : str
            Name or alias of the resource to open.
        """
        self._dp832 = self._resourceManager.open_resource(resource_name)  # type: MessageBasedResource
        self._dp832.read_termination = '\n'
        self.instrument = Instrument(self._dp832)
        self.output = Output(self._dp832)
        self.timer = Timer(self._dp832)
        self.source = Source(self._dp832)

    def close(self):
        """ Close the resource manager session. """
        self._dp832.close()

    def clear(self):
        """ Send command that clears all the event registers """
        self._dp832.write('*cls')

    def reset(self):
        """ Send command that restores the power supply to factory state and clears the error queue """
        self._dp832.write('*rst')

    def query_id(self) -> str:
        """ Send command that queries the ID string of the instrument """
        return self._dp832.query('*idn?')

    def init(self):
        """ Send command that initializes the trigger system """
        self._dp832.write('INIT')

    def wait(self):
        """ Send command that sets the instrument to executing any other command after all the pending
        operations are completed. """
        self._dp832.write('*WAI')

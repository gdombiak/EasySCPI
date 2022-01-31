from pyvisa import ResourceManager
from pyvisa.resources import MessageBasedResource

from dmm6500.Sense import Sense
from dmm6500.Trace import Trace
from dmm6500.Trigger import Trigger


class DMM6500:
    def __init__(self, resource_manager: ResourceManager) -> None:
        super().__init__()
        self._resourceManager = resource_manager
        self._dmm = None
        self.trace: Trace = None
        self.trigger: Trigger = None
        self.sense: Sense = None

    def open(self, resource_name: str):
        """ Return an instrument for the resource name. A session will be created.

        Parameters
        ----------
        resource_name : str
            Name or alias of the resource to open.
        """
        self._dmm = self._resourceManager.open_resource(resource_name)  # type: MessageBasedResource
        self._dmm.timeout = 5000  # ms
        self._dmm.encoding = 'latin_1'
        self._dmm.read_termination = '\n'
        self._dmm.write_termination = None
        self.trace = Trace(self._dmm)
        self.trigger = Trigger(self._dmm)
        self.sense = Sense(self._dmm)

    def close(self):
        """ Close the resource manager session. """
        self._dmm.close()

    def clear(self):
        """ Send command that clears the event registers and queues """
        self._dmm.write('*cls')  # clear ESR

    def reset(self):
        """ Send command that resets the instrument settings to their default values and clears the reading buffers """
        self._dmm.write('*rst')  # Reset the DMM6500

    def query_id(self) -> str:
        """ Send command that retrieves the identification string of the instrument """
        return self._dmm.query('*idn?')

    def init(self):
        """ Send command that starts the trigger model or scan. """
        self._dmm.write('INIT')

    def wait(self):
        """ Send command that postpones the execution of subsequent commands until all previous overlapped
        commands are finished. """
        self._dmm.write('*WAI')

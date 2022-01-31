from enum import Enum


class VoltUnit(Enum):
    VOLT = 1
    MILLI = 2
    MICRO = 3

    def convert(self, value: float) -> str:
        if self.value == 1:
            return '{:0=12.9f}'.format(value / 1e-0)
        elif self.value == 2:
            return '{:0=8.4f}'.format(value / 1e-3)
        else:
            return '{:0=8.4f}'.format(value / 1e-6)

    def unit(self) -> str:
        if self.value == 1:
            return 'V'
        elif self.value == 2:
            return 'mV'
        else:
            return 'µV'


class CurrentUnit(Enum):
    AMP = 1
    MILLI = 2
    MICRO = 3

    def convert(self, value: float) -> str:
        if self.value == 1:
            return '{:0=12.9f}'.format(value / 1e-0)
        elif self.value == 2:
            return '{:0=8.4f}'.format(value / 1e-3)
        else:
            return '{:0=8.4f}'.format(value / 1e-6)

    def unit(self) -> str:
        if self.value == 1:
            return 'A'
        elif self.value == 2:
            return 'mA'
        else:
            return 'µA'

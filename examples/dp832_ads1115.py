import pyvisa as visa

from dp832.DP832 import DP832

rm = visa.ResourceManager()
try:
    dp832 = DP832(rm)
    dp832.open('TCPIP::192.168.252.18::INSTR')
    dp832.clear()
    print(dp832.query_id())

    # Turn off timer so we can set configuration
    dp832.timer.turn_on(False)

    # Select channel 1, set Timer configuration and enable it
    dp832.instrument.nselect(1)
    dp832.timer.cycles(1)
    dp832.timer.groups(5)
    dp832.timer.parameter(0, 4.2, 1, 5)
    dp832.timer.parameter(1, 3.8, 1, 5)
    dp832.timer.parameter(2, 3.2, 1, 5)
    dp832.timer.parameter(3, 3.0, 1, 5)
    dp832.timer.parameter(4, 2.9, 1, 5)
    dp832.timer.turn_off_when_done(True)
    dp832.output.turn_on(1, True)
    dp832.timer.turn_on(True)

    # Select channel 2, set Timer configuration and enable it
    dp832.instrument.nselect(2)
    dp832.timer.cycles(1)
    dp832.timer.groups(5)
    dp832.timer.parameter(0, 2.2, 1, 5)
    dp832.timer.parameter(1, 2.8, 1, 5)
    dp832.timer.parameter(2, 3.2, 1, 5)
    dp832.timer.parameter(3, 3.8, 1, 5)
    dp832.timer.parameter(4, 4.2, 1, 5)
    dp832.timer.turn_off_when_done(True)
    dp832.output.turn_on(2, True)
    dp832.timer.turn_on(True)

    # print(timer.query_cycles())
    # print(timer.query_groups())

    dp832.close()                   # Close session

except visa.VisaIOError as err:
    print("Failed to open resource. Error: ", err)

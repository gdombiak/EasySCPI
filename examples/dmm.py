import time

import pyvisa as visa

from dmm6500.DMM6500 import DMM6500
from dmm6500.Sense import Function
from dmm6500.Trace import Element

rm = visa.ResourceManager()
try:
    read_seconds = 5

    dmm = DMM6500(rm)
    dmm.open('TCPIP::192.168.252.20::INSTR')
    dmm.clear()
    dmm.reset()
    print(dmm.query_id())

    dmm.sense.function(Function.VOLTAGE_DC)     # Configure to Measure VDC
    dmm.trigger.duration_loop(read_seconds, 0, "defbuffer1")  # Trigger model will measure for 5 seconds
    dmm.init()                   # Start the trigger model
    dmm.wait()                   # Wait for the trigger model to complete
    time.sleep(read_seconds)

    max_read_data = dmm.trace.actual("defbuffer1")
    dmm_values = dmm.trace.data(max_read_data, "defbuffer1", Element.READING).split(',')
    dmm_timestamps = dmm.trace.data(max_read_data, "defbuffer1", Element.RELATIVE).split(',')

    # Convert from string to float
    for i in range(0, len(dmm_timestamps)):
        dmm_timestamps[i] = float(dmm_timestamps[i])
        dmm_values[i] = float(dmm_values[i])

    print(dmm.trace.stats_average("defbuffer1"))
    print(dmm.trace.stats_max("defbuffer1"))
    print(dmm.trace.stats_min("defbuffer1"))
    print(dmm.trace.stats_peak_to_peak("defbuffer1"))

    dmm.close()                         # Close session

    # dmm.write(':SENS:FUNC "VOLT:DC"')   # Set the instrument to measure DC voltage
    # dmm.write(':SENS:VOLT:RANG 10')     # Set the measure range to 10 V
    # dmm.write(':SENS:VOLT:INP AUTO')    # Set the input impedance to auto so the instrument selects 10 Ω for the 10 V range
    # dmm.write(':SENS:VOLT:NPLC 10')     # Set the integration rate (NPLCs) to 10
    # dmm.write(':SENS:VOLT:AZER ON')     # Enable autozero
    # dmm.write(':SENS:VOLT:AVER:TCON REP')   # Set the averaging filter type to repeating
    # dmm.write(':SENS:VOLT:AVER:COUN 100')   # Set the filter count to 100
    # dmm.write(':SENS:VOLT:AVER ON')     # Enable the filter
    # dmm.write(':READ?')                 # Read the voltage value; it is a few seconds before the reading is returned
except visa.VisaIOError as err:
    print("Failed to open resource. Error: ", err)

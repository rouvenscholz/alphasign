"""
Here is a simple example for controlling a Betabrite Prism via USB::

  import time
  import alphasign


  def main():
    sign = alphasign.USB(alphasign.devices.USB_BETABRITE_PRISM)
    sign.connect()
    sign.clear_memory()

    # create logical objects to work with
    counter_str = alphasign.String(size=14, label="1")
    counter_txt = alphasign.Text("counter value: %s%s" % (alphasign.colors.RED,
                                                          counter_str.call()),
                                 label="A",
                                 mode=alphasign.modes.HOLD)

    # allocate memory for these objects on the sign
    sign.allocate((counter_str, counter_txt))

    # tell sign to only display the counter text
    sign.set_run_sequence((counter_txt,))

    # write objects
    for obj in (counter_str, counter_txt):
      sign.write(obj)

    # (strictly) monotonically increasing counter
    counter_value = 0
    while True:
      counter_str.data = counter_value
      sign.write(counter_str)
      counter_value += 1
      time.sleep(1)


  if __name__ == "__main__":
    main()
"""
import datetime
import os
import sys
import serial

import alphasign.constants
from alphasign.interfaces.local import DebugInterface
from alphasign.interfaces.local import Serial
from alphasign.interfaces.local import USB

from alphasign.time import Time
from alphasign.date import Date
from alphasign.string import String
from alphasign.packet import Packet
from alphasign.text import Text
from alphasign.smalldots import SmallDotsPicture

import alphasign.charsets
import alphasign.colors
import alphasign.counters
import alphasign.devices
import alphasign.extchars
import alphasign.modes
import alphasign.positions
import alphasign.speeds



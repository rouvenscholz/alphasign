"""
The following constants are defined to change speeds in TEXT
(:class:`alphasign.text.Text`) files:

* :const:`SPEED_1` (slowest)
* :const:`SPEED_2`
* :const:`SPEED_3`
* :const:`SPEED_4`
* :const:`SPEED_5` (fastest)

--------
Examples
--------

Make a text file with fast text::

  msg = alphasign.Text("%sthis text is fast" % alphasign.speeds.SPEED_5,
                       label="A",
                       mode=alphasign.modes.ROTATE)
"""

# Display speeds
SPEED_1 = b"\x15"
SPEED_2 = b"\x16"
SPEED_3 = b"\x17"
SPEED_4 = b"\x18"
SPEED_5 = b"\x19"

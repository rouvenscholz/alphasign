"""
The following constants are defined to change TEXT
(:class:`alphasign.text.Text`) colors:

* :const:`RED`
* :const:`GREEN`
* :const:`AMBER`
* :const:`DIM_RED`
* :const:`DIM_GREEN`
* :const:`BROWN`
* :const:`ORANGE`
* :const:`YELLOW`
* :const:`RAINBOW_1`
* :const:`RAINBOW_2`
* :const:`COLOR_MIX`
* :const:`AUTOCOLOR`

.. autofunction:: rgb
.. autofunction:: shadow_rgb

--------
Examples
--------

Make a text file with red text::

  msg = alphasign.Text("%sthis text is red" % alphasign.colors.RED, label="A")

Make a text file with purple text (#CC66FF)::

  msg = alphasign.Text("%sthis text should be in purple" %
                       alphasign.colors.rgb("CC66FF"), label="A")

Make a bi-color text file (red primary with a green shadow)::

  msg = alphasign.Text("%s%sred and green" %
                       (alphasign.colors.rgb("FF0000"),
                        alphasign.colors.rgb("00FF00")), label="A")
"""

# Colors
NONE      = b"\x1C0"
RED       = b"\x1C1"
GREEN     = b"\x1C2"
AMBER     = b"\x1C3"
DIM_RED   = b"\x1C4"
DIM_GREEN = b"\x1C5"
BROWN     = b"\x1C6"
ORANGE    = b"\x1C7"
YELLOW    = b"\x1C8"
RAINBOW_1 = b"\x1C9"
RAINBOW_2 = b"\x1CA"
COLOR_MIX = b"\x1CB"
AUTOCOLOR = b"\x1CC"


def rgb(rgb):
  """
  Create color constant for use in TEXT and STRING files.

  :param rgb: 6-character hex string in form RRGGBB.
  """
  if len(rgb) and rgb[0] == b"#":
    rgb = rgb[1:]
  return b"\x1CZ%s" % rgb


def shadow_rgb(rgb):
  """
  Create shadow color constant for use in TEXT and STRING files.

  :param rgb: 6-character hex string in form RRGGBB.
  """
  if len(rgb) and rgb[0] == b"#":
    rgb = rgb[1:]
  return b"\x1CY%s" % rgb

"""
Character constants can be used to change the font style in TEXT
(:class:`alphasign.text.Text`) and STRING (:class:`alphasign.string.String`)
files.

--------------
Character sets
--------------

The following character set constants are defined:

* :const:`FIVE_HIGH_STD`
* :const:`FIVE_STROKE`
* :const:`SEVEN_HIGH_STD`
* :const:`SEVEN_STROKE`
* :const:`SEVEN_HIGH_FANCY`
* :const:`TEN_HIGH_STD`
* :const:`SEVEN_SHADOW`
* :const:`FULL_HEIGHT_FANCY`
* :const:`FULL_HEIGHT_STD`
* :const:`SEVEN_SHADOW_FANCY`
* :const:`FIVE_WIDE`
* :const:`SEVEN_WIDE`
* :const:`SEVEN_FANCY_WIDE`
* :const:`WIDE_STROKE_FIVE`

The following character sets are available only on Alpha 2.0 and 3.0 protocols:

* :const:`FIVE_HIGH_CUST`
* :const:`SEVEN_HIGH_CUST`
* :const:`TEN_HIGH_CUST`
* :const:`FIFTEEN_HIGH_CUST`

--------------------
Character attributes
--------------------

The following character attribute constants are defined:

* :const:`WIDE_ON`
* :const:`WIDE_OFF`
* :const:`DOUBLE_WIDE_ON`
* :const:`DOUBLE_WIDE_OFF`
* :const:`DOUBLE_HIGH_ON`
* :const:`DOUBLE_HIGH_OFF`
* :const:`TRUE_DESCENDERS_ON`
* :const:`TRUE_DESCENDERS_OFF`
* :const:`FIXED_WIDTH_ON`
* :const:`FIXED_WIDTH_OFF`
* :const:`FANCY_ON`
* :const:`FANCY_OFF`
* :const:`AUXILIARY_PORT_ON` -- Series 4000 & 7000 signs only.
* :const:`AUXILIARY_PORT_OFF`
* :const:`SHADOW_CHARACTERS_ON` -- Betabrite model 1036 and AlphaPriemere 9000 signs only.
* :const:`SHADOW_CHARACTERS_OFF`

-----------------
Character spacing
-----------------

The following character spacing constants are defined:

* :const:`PROPORTIONAL` -- default
* :const:`FIXED_WIDTH` -- fixed width left justified

--------
Examples
--------

Make a text file using the :const:`FIVE_WIDE` charset::

  msg = alphasign.Text("%sthis is wide" % alphasign.charsets.FIVE_WIDE,
                       label="A")

"""

# Character sets
FIVE_HIGH_STD         = b"\x1A1"
FIVE_STROKE           = b"\x1A2"
SEVEN_HIGH_STD        = b"\x1A3"
SEVEN_STROKE          = b"\x1A4"
SEVEN_HIGH_FANCY      = b"\x1A5"
TEN_HIGH_STD          = b"\x1A6"
SEVEN_SHADOW          = b"\x1A7"
FULL_HEIGHT_FANCY     = b"\x1A8"
FULL_HEIGHT_STD       = b"\x1A9"
SEVEN_SHADOW_FANCY    = b"\x1A:"
FIVE_WIDE             = b"\x1A;"
SEVEN_WIDE            = b"\x1A<"
SEVEN_FANCY_WIDE      = b"\x1A="
WIDE_STROKE_FIVE      = b"\x1A>"

# Alpha 2.0 and 3.0 only
FIVE_HIGH_CUST        = b"\x1AW"
SEVEN_HIGH_CUST       = b"\x1AX"
TEN_HIGH_CUST         = b"\x1AY"
FIFTEEN_HIGH_CUST     = b"\x1AZ"

# Character attributes
WIDE_ON               = b"\x1D01"
WIDE_OFF              = b"\x1D00"
DOUBLE_WIDE_ON        = b"\x1D11"
DOUBLE_WIDE_OFF       = b"\x1D10"
DOUBLE_HIGH_ON        = b"\x1D21"
DOUBLE_HIGH_OFF       = b"\x1D20"
TRUE_DESCENDERS_ON    = b"\x1D31"
TRUE_DESCENDERS_OFF   = b"\x1D30"
FIXED_WIDTH_ON        = b"\x1D41"
FIXED_WIDTH_OFF       = b"\x1D40"
FANCY_ON              = b"\x1D51"
FANCY_OFF             = b"\x1D50"
AUXILIARY_PORT_ON     = b"\x1D61"
AUXILIARY_PORT_OFF    = b"\x1D60"
SHADOW_CHARACTERS_ON  = b"\x1D71"
SHADOW_CHARACTERS_OFF = b"\x1D70"

FLASH_ON              = b"\x071"
FLASH_OFF             = b"\x070"

# Character spacing
PROPORTIONAL          = b"\x1E0"
FIXED_WIDTH           = b"\x1E1"

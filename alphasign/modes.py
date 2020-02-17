"""
This module defines available modes for use with TEXT files
(:class:`alphasign.text.Text`).

The following display modes are defined:

* :const:`ROTATE`
* :const:`HOLD`
* :const:`ROLL_UP`
* :const:`ROLL_DOWN`
* :const:`ROLL_LEFT`
* :const:`ROLL_RIGHT`
* :const:`WIPE_UP`
* :const:`WIPE_DOWN`
* :const:`WIPE_LEFT`
* :const:`WIPE_RIGHT`
* :const:`SCROLL`
* :const:`AUTOMODE`
* :const:`ROLL_IN`
* :const:`ROLL_OUT`
* :const:`WIPE_IN`
* :const:`WIPE_OUT`
* :const:`COMPRESSED_ROTATE` (works only on certain sign models)
* :const:`EXPLODE` (Alpha 3.0 protocol only)
* :const:`CLOCK` (Alpha 3.0 protocol only)

The following special modes are defined:

* :const:`TWINKLE`
* :const:`SPARKLE`
* :const:`SNOW`
* :const:`INTERLOCK`
* :const:`SWITCH`
* :const:`SLIDE` (only Betabrite 1036)
* :const:`SPRAY`
* :const:`STARBURST`
* :const:`WELCOME`
* :const:`SLOT_MACHINE`
* :const:`NEWS_FLASH` (only Betabrite 1036)
* :const:`TRUMPET_ANIMATION` (only Betabrite (1036)
* :const:`CYCLE_COLORS` (only AlphaEclipse 3600)

Special graphics are modes which display graphics before the message. The
following special graphics are defined:

* :const:`THANK_YOU`
* :const:`NO_SMOKING`
* :const:`DONT_DRINK_DRIVE`
* :const:`RUNNING_ANIMAL`
* :const:`FISH_ANIMATION`
* :const:`FIREWORKS`
* :const:`TURBO_CAR`
* :const:`BALLOON_ANIMATION`
* :const:`CHERRY_BOMB`

--------
Examples
--------

Make a text file stationary on the sign::

  msg = alphasign.Text("hello world", label="A", mode=alphasign.modes.HOLD)

To change the mode for an already created text file, do::

  msg.mode = alphasign.modes.ROLL_IN
"""

# Normal display modes
ROTATE            = b"a"
HOLD              = b"b"
FLASH             = b"c"
ROLL_UP           = b"e"
ROLL_DOWN         = b"f"
ROLL_LEFT         = b"g"
ROLL_RIGHT        = b"h"
WIPE_UP           = b"i"
WIPE_DOWN         = b"j"
WIPE_LEFT         = b"k"
WIPE_RIGHT        = b"l"
SCROLL            = b"m"
AUTOMODE          = b"o"
ROLL_IN           = b"p"
ROLL_OUT          = b"q"
WIPE_IN           = b"r"
WIPE_OUT          = b"s"
COMPRESSED_ROTATE = b"t"
EXPLODE           = b"u"
CLOCK             = b"v"

# Special modes
TWINKLE           = b"n0"
SPARKLE           = b"n1"
SNOW              = b"n2"
INTERLOCK         = b"n3"
SWITCH            = b"n4"
SLIDE             = b"n5"
SPRAY             = b"n6"
STARBURST         = b"n7"
WELCOME           = b"n8"
SLOT_MACHINE      = b"n9"
NEWS_FLASH        = b"nA"
TRUMPET_ANIMATION = b"nB"
CYCLE_COLORS      = b"nC"

# Special graphics
THANK_YOU         = b"nS"
NO_SMOKING        = b"nU"
DONT_DRINK_DRIVE  = b"nV"
RUNNING_ANIMAL    = b"nW"
FISH_ANIMATION    = b"nW"
FIREWORKS         = b"nX"
TURBO_CAR         = b"nY"
BALLOON_ANIMATION = b"nY"
CHERRY_BOMB       = b"nZ"

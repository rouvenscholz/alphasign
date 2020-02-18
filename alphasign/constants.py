# Command Codes
WRITE_TEXT            = b"A"  # Write TEXT file (p18)
READ_TEXT             = b"B"  # Read TEXT file (p19)
WRITE_SPECIAL         = b"E"  # Write SPECIAL FUNCTION commands (p21)
READ_SPECIAL          = b"F"  # Read SPECIAL FUNCTION commands (p29)
WRITE_STRING          = b"G"  # Write STRING (p37)
READ_STRING           = b"H"  # Read STRING (p38)
WRITE_SMALL_DOTS      = b"I"  # Write SMALL DOTS PICTURE file (p39)
READ_SMALL_DOTS       = b"J"  # Read SMALL DOTS PICTURE file (p41)
WRITE_RGB_DOTS        = b"K"  # Write RGB DOTS PICTURE file (p44)
READ_RGB_DOTS         = b"L"  # Read RGB DOTS PICTURE file (p46)
WRITE_LARGE_DOTS      = b"M"  # Write LARGE DOTS PICTURE file (p42)
READ_LARGE_DOTS       = b"N"  # Read LARGE DOTS PICTURE file (p43)
WRITE_ALPHAVISION     = b"O"  # Write ALPHAVISION BULLETIN (p48)
SET_TIMEOUT           = b"T"  # Set Timeout Message (p118) (Alpha 2.0/3.0)

UNLOCKED              = b"U"
LOCKED                = b"L"

# Constants used in transmission packets
NUL                   = b"\x00"  # NULL
SOH                   = b"\x01"  # Start of Header
STX                   = b"\x02"  # Start of TeXt (precedes a command code)
ETX                   = b"\x03"  # End of TeXt
EOT                   = b"\x04"  # End Of Transmission
#ENQ                   = b"\x05"  # Enquiry
#ACK                   = b"\x06"  # Acknowledge
BEL                   = b"\x07"  # Bell
BS                    = b"\x08"  # Backspace
HT                    = b"\x09"  # Horizontal tab
LF                    = b"\x0A"  # Line Feed
NL                    = b"\x0A"  # New Line
VT                    = b"\x0B"  # Vertical Tab
#FF                    = b"\x0C"  # Form Feed
NP                    = b"\x0C"  # New Page
CR                    = b"\x0D"  # Carriage Return
CAN                   = b"\x18"  # Cancel
SUB                   = b"\x1A"  # Substitute (select charset)
ESC                   = b"\x1B"  # Escape character

NEWLINE               = NL
NEWPAGE               = NP

# Constants for SMALL DOTS PICTURE color palette
TYPE_MONOCHROME       = b"1000"
TYPE_3COLOR           = b"2000"
TYPE_8COLOR           = b"4000"

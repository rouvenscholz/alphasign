import time

from alphasign import constants
from alphasign import packet

import alphasign.string
import alphasign.text


class BaseInterface(object):
  """Base interface from which all other interfaces inherit.

  This class contains utility methods for fundamental sign features.
  """

  def write(self, data):
    return False
  
  def read(self, size):
    return False

  def clear_memory(self):
    """Clear the sign's memory.

    :rtype: None
    """
#    pkt = packet.Packet("%s%s" % (constants.WRITE_SPECIAL, "$"))
    pkt = packet.Packet(b"".join([constants.WRITE_SPECIAL,b"$"]))
    self.write(pkt)
    time.sleep(1)

  def beep(self, frequency=0, duration=0.1, repeat=0):
    """Make the sign beep.

    :param frequency: frequency integer (not in Hz), 0 - 254
    :param duration: beep duration, 0.1 - 1.5
    :param repeat: number of times to repeat, 0 - 15

    :rtype: None
    """
    if frequency < 0:
      frequency = 0
    elif frequency > 254:
      frequency = 254

    duration = int(duration / 0.1)
    if duration < 1:
      duration = 1
    elif duration > 15:
      duration = 15

    if repeat < 0:
      repeat = 0
    elif repeat > 15:
      repeat = 15

    pkt = packet.Packet(b"%s%s%02X%X%X" % (constants.WRITE_SPECIAL, "(2",
                                          frequency, duration, repeat))
    self.write(pkt)

  def soft_reset(self):
    """Perform a soft reset on the sign.

    This is non-destructive and does not clear the sign's memory.

    :rtype: None
    """
    pkt = packet.Packet("%s%s" % (constants.WRITE_SPECIAL, ",").encode())
    self.write(pkt)

  def allocate(self, files):
    """Allocate a set of files on the device.

    :param files: list of file objects (:class:`alphasign.text.Text`,
                                        :class:`alphasign.string.String`, ...)

    :rtype: None
    """
    seq = b""
    for obj in files:
      # format: FTPSIZEQQQQ

      if type(obj) == alphasign.string.String:
        file_type = b"B"
        qqqq = b"0000"  # unused for strings
        size_hex = b"%04X" % obj.size
        lock = constants.LOCKED
      elif type(obj) == alphasign.smalldots.SmallDotsPicture:
        file_type = b"D"
        qqqq = obj.typ
        size_hex = b"%02X%02X" % (obj.height, obj.width)
        lock = constants.LOCKED
      else:  # if type(obj) == alphasign.text.Text:
        file_type = b"A"
        qqqq = b"FFFF"  # TODO(ms): start/end times
        size_hex = b"%04X" % obj.size
        lock = constants.UNLOCKED

#      alloc_str = ("%s%s%s%s%s" %
#                   (obj.label,  # file label to allocate
#                   file_type,   # file type
#                   lock,
#                   size_hex,    # size in hex
#                   qqqq))
      seq = b"".join([
        seq, obj.label, file_type, lock, size_hex, qqqq
      ])

    # allocate special TARGET TEXT files 1 through 5
    for i in range(5):
#      alloc_str = ("%s%s%s%s%s" %
#                   ("%d" % (i + 1),
#                   "A",    # file type
#                   constants.UNLOCKED,
#                   "%04X" % 100,
#                   "FEFE"))
#      seq += alloc_str
      seq = b"".join([
        seq, 
        b"%d" % (i + 1), 
        b"A",  #file type
        constants.UNLOCKED, 
        b"%04X" % 100, 
        b"FEFE"
      ])
#    seq = seq.encode()

#    pkt = packet.Packet("%s%s%s" % (constants.WRITE_SPECIAL, "$", seq))
    pkt = packet.Packet(b"".join([
        constants.WRITE_SPECIAL,
        b"$",
        seq
    ]))
    self.write(pkt)

  def set_run_sequence(self, files, locked=False):
    """Set the run sequence on the device.

    This determines the order in which the files are displayed on the device, if
    at all. This is useful when handling multiple TEXT files.

    :param files: list of file objects (:class:`alphasign.text.Text`,
                                        :class:`alphasign.string.String`, ...)
    :param locked: allow sequence to be changed with IR keyboard

    :rtype: None
    """
#    seq_str = ".T"
#    seq_str += locked and "L" or "U"
    seq_str = b"".join([
      b"T", 
      locked and b"L" or b"U"
    ])
    for obj in files:
#      seq_str += obj.label
      seq_str = b"".join([seq_str, obj.label])
    #pkt = packet.Packet("%s%s" % (constants.WRITE_SPECIAL, seq_str))
    pkt = packet.Packet(b"".join([constants.WRITE_SPECIAL, seq_str]))
    self.write(pkt)

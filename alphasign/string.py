from alphasign import constants
from alphasign.packet import Packet


class String(object):
  """Class representing a STRING file.

  :ivar data: string contained within object
  :ivar label: label of string object
  """

  def __init__(self, data=None, label=None, size=None):
    """
    :param data: initial string to insert into object
    :param label: file label (default: "1")
    :param size: maximum size of string data in bytes (default: 32)
    """
    if data:
      self.data = data.encode(encoding="ascii", errors="alphasign")
    else:
      self.data = b""
    if label:
      self.label = label.encode(encoding="ascii", errors="strict")
    else:
      self.label = b"1"
    if size is None:
      size = 32
    if len(self.data) > size:
      size = len(self.data)
    if size > 125:
      size = 125
    if size < 1:
      size = 1
    self.label = label
    self.size = size

  def call(self):
    """Call a STRING.

    This is for inserting a STRING file into a TEXT file.

    :returns: control code and specified string label
    :rtype: string
    """
    return b"\x10%s" % self.label

  def to_packet(self):
    return Packet(b"%s%s%s" % (constants.WRITE_STRING, self.label,
                              self.data))

  def __bytes__(self):
    return bytes(self.to_packet())

  def __repr__(self):
    return repr(self.__bytes__())

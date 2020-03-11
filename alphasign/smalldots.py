from alphasign import constants
from alphasign.packet import Packet

class SmallDotsPicture(object):
  """Class representing a SMALL DOTS PICTURE file.

  :ivar height: height of picture
  :ivar width: width of picture
  :ivar typ: color palette type of picture
  :ivar label: label of small dots picture object
  """

  def __init__(self, height, width, typ=None, label=None):
    """
    :param height: height of the picture
    :param width: width of the picture
    :param typ: color palette type of picture (default: 8-color)
    :param label: file label (default: "1")
    """
    if typ is None:
      typ = constants.TYPE_8COLOR
    if label is None:
      label = b"a"
    if height > 31:
        height = 31
    if height < 0:
        height = 0
    if width > 255:
        width = 255
    if width < 0:
        width = 0
    self.height = height
    self.width = width
    self.typ = typ
    self.label = label.encode(encoding="ascii", errors="strict")
    self.data = [[0 for _ in range(width)] for _ in range(height)]

  def set_pixel(self, x, y, color):
    """Set color of pixel.

    :param x: x-axis coordinate
    :param y: y-axis coordinate
    :param color: pixel color index from 0 - 8
    """
    if type(color) == int:
      self.data[y][x] = color
    else:
      self.data[y][x] = color[1] # expect "\x1C0" constants from colors module.
    
  def get_pixel(self, x, y):
    """Get color of pixel.

    :param x: x-axis coordinate
    :param y: y-axis coordinate
    :returns: Color index from 0 - 8.
    :rtype: int
    """
    return self.data[y][x]

  def call(self):
    """Call a STRING.

    This is for inserting a STRING file into a TEXT file.

    :returns: control code and specified string label
    :rtype: string
    """
    return b"\x14%s" % self.label

  def to_packet(self):
    image_data = b''
    for line in self.data:
        image_data += b''.join(str(col).encode() for col in line) + b'\r'
    pkt = Packet()
    header = b"%s%s%02X%02X" % (constants.WRITE_SMALL_DOTS, self.label,
                                  self.height, self.width)
    pkt.add_part(header, delay=150) # min. 100ms delay after sending the width
    pkt.add_part(image_data)
    return pkt

  def __bytes__(self):
    return bytes(self.to_packet())

  def __repr__(self):
    return repr(self.__bytes__())

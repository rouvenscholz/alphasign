from alphasign import constants
from alphasign import modes
from alphasign import positions
from alphasign.packet import Packet


class Text(object):
  """Class representing a TEXT file.

  This class is aliased as :class:`alphasign.Text` in :mod:`alphasign.__init__`.
  """

  def __init__(self, data=None, label=None, size=None,
               position=None, mode=None, priority=False):
    """
    :param data: initial string to insert into object
    :param label: file label (default: "A")
    :param size: amount of bytes to allocate for object on sign (default: 64)
    :param position: constant from :mod:`alphasign.positions`
    :param mode: constant from :mod:`alphasign.modes`
    :param priority: set this text to be displayed instead of
                     all other TEXT files. Set to True with an empty message to
                     clear a priority TEXT.
    """
    if data:
      self.data = data.encode(encoding="ascii", errors="alphasign")
    else:
      self.data = b""
    if label:
       self.label = label.encode(encoding="ascii", errors="strict")
    else:
      self.label = b"A"
    if size is None:
      size = 64
    if len(self.data) > size:
      size = len(self.data)
    if size < 1:
      size = 1
    if position is None:
      position = positions.MIDDLE_LINE
    if mode is None:
      mode = modes.ROTATE

    self.size = size
    self.position = position
    self.mode = mode
    self.priority = priority

  def to_packet(self):
    # [WRITE_TEXT][File Label][ESC][Display Position][Mode Code]
    #   [Special Specifier][ASCII Message]
    if self.data:
      packet = b"".join([
        constants.WRITE_TEXT,
        self.priority and b"0" or self.label,
        constants.ESC,
        self.position,
        self.mode,
        self.data
      ])
    else:
#      packet = Packet("%s%s" % (constants.WRITE_TEXT,
#                                (self.priority and "0" or self.label)))
      packet = Packet(b"".join([constants.WRITE_TEXT, self.priority and b"0" or self.label]))
    return packet

  def __bytes__(self):
    return self.to_packet()

  def __repr__(self):
    return repr(self.__bytes__())

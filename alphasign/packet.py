from alphasign import constants

class PacketPart(object):
  """Small helper class to split a packet into several chunks with delays inbetween.

  This class allows to delay sending more data mid-packet
  if the protocol has timing requirements.
  :ivar contents: Package data.
  :ivar delay: sleep (milliseconds) after sending this part
  """
  def __init__(self, contents, delay=0):
    self.contents = contents
    self.delay = delay
  
  def __bytes__(self):
    #return self.contents.encode()
    return self.contents

class Packet(object):
  """Container for data to be sent to a sign device.

  Packet objects are created by other classes and should not usually be
  instantiated directly.
  """

  def __init__(self, contents=None):
    self.type     = b"Z"   # Type Code (see protocol)
    self.address  = b"00"  # Sign Address (see protocol)
    self._pkt = []
    if contents is not None:
      self._pkt.append(PacketPart(contents))

  def add_part(self, contents, delay=0):
    self._pkt.append(PacketPart(contents, delay))
  
  def get_parts(self):
    parts = []
    # Add base protocol packet header
#    parts.append(PacketPart("%s%s%s%s%s" %
#              (constants.NUL * 5, constants.SOH, self.type,
#                self.address, constants.STX)))
    parts.append(PacketPart(b"".join([
        constants.NUL * 5, constants.SOH, self.type,
        self.address, constants.STX
    ])))
    # Add all payload parts
    for part in self._pkt:
      parts.append(part)
    # Add base protocol end indicator without checksums.
    parts.append(PacketPart(constants.EOT))
    return parts

  def __bytes__(self):
    data = b""
    for part in self.get_parts():
      data += bytes(part)
    return data

  def __repr__(self):
    return repr(self.__bytes__())

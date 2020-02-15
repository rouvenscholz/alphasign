from codecs import register_error
from sys import stderr

class StringEncoder:
  __lookup = None

  @staticmethod
  def init():
    def calccode(charcode):
      return bytes([0x08, charcode - 0x60])
    if not StringEncoder.__lookup:
      StringEncoder.__lookup = {
        "Ç": calccode(128),
        "ü": calccode(129),
        "é": calccode(130),
        "â": calccode(131), 
        "ä": calccode(132),
        "à": calccode(133),
        "å": calccode(134),
        "ç": calccode(135),
        "ê": calccode(136),
        "ë": calccode(137),
        "è": calccode(138),
        "ï": calccode(139),
        "î": calccode(140),
        "ì": calccode(141),
        "Ä": calccode(142),
        "Å": calccode(143),
        "É": calccode(144),
        "æ": calccode(145),
        "Æ": calccode(146),
        "ô": calccode(147),
        "ö": calccode(148),
        "ò": calccode(149),
        "û": calccode(150),
        "ù": calccode(151),
        "ÿ": calccode(152),
        "Ö": calccode(153),
        "Ü": calccode(154),
        "¢": calccode(155),
        "£": calccode(156),
        "¥": calccode(157),
        "Ʀ": calccode(158),
        "ſ": calccode(159),
#        "å": calccode(160),  # difference to 134 is only one pixel. what is the correct unicode? 
        "í": calccode(161),
        "ó": calccode(162),
        "ú": calccode(163),
        "ñ": calccode(164),
        "Ñ": calccode(165),
        "ª": calccode(166),
        "º": calccode(167),
        "¿": calccode(168),
        "°": calccode(169),
        "¡": calccode(170),
 #       "": calccode(171), # is this a special space (e.g. NO-BREAK SPACE)?
        "ø": calccode(172),
        "Ø": calccode(173),
        "ć": calccode(174),
        "Ć": calccode(175),
        "č": calccode(176),
        "Č": calccode(177),
        "ð": calccode(178),
        "Ð": calccode(179),
        "š": calccode(180),
        "ž": calccode(181),
        "Ž": calccode(182),
        "ẞ": calccode(183),  # big sharp S
        "Š": calccode(184),
        "ß": calccode(185),
        "Á": calccode(186),
        "À": calccode(187),
        "Ã": calccode(188),
        "ã": calccode(189),
        "Ê": calccode(190),
        "Í": calccode(191),
        "Õ": calccode(192),
        "õ": calccode(193),
        "€": calccode(194)
      }
      register_error("alphasign", StringEncoder.__asciierrorhandler)

 

  def __asciierrorhandler(err):
    result = b""
    for i in range(err.start, err.end):
      try:
        result = b"".join([result, StringEncoder.__lookup[err.object[i]]])
      except KeyError:
        print("unsupported character used: '{}'".format(err.object[i]), file=stderr)
        result = b"".join([result, b"?"])
    return (result, err.end)



def main():
  from sys import argv
  StringEncoder.init()
  s = argv[1] if len(argv) >= 2 else argv[0]
  s = s.encode(encoding='ascii', errors="alphasign")
  print(s)

if __name__ == '__main__':
  main()

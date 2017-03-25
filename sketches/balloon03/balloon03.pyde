def setup():
    size(400, 400)
    a = [0xE5, 0xBC, 0x97]
    balloon = "".join([chr(c) for c in a]).decode("UTF-8")
    textSize(40)
    text(balloon, width/2, height/2)



# "BALLOON
# Unicode: U+1F388 (U+D83C U+DF88), UTF-8: F0 9F 8E 88
# Ⓠ
# CIRCLED LATIN CAPITAL LETTER Q
# Unicode: U+24C6, UTF-8: E2 93 86
# $
# DOLLAR SIGN
# Unicode: U+0024, UTF-8: 24
# 弗
# CJK UNIFIED IDEOGRAPH-5F17
# Unicode: U+5F17, UTF-8: E5 BC 97
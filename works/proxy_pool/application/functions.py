# 字符串解密
def rot13(message):
    res = ''
    for item in message:
        if (item >= 'A' and item <= 'M') or (item >= 'a' and item <= 'm'):
            res += chr(ord(item) + 13)
        elif (item >= 'N' and item <= 'Z') or (item >= 'n' and item <= 'z'):
            res += chr(ord(item) - 13)
        else:
            res += item
    return res
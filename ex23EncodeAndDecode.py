# example of string encoding in python
import base64
string1 = "This is example of encoding"
string2 = "河內的實施了調查波士頓"
# 在编码字符串的时候 想要把字符串转换为 utf-8 的二进制字节格式
# 想要字符串到字节  就是编码
# 想要字节到字符串  就是解码
stringEncodedBig5 = string2.encode("Big5", 'strict')
stringEncodedUtf8 = string1.encode("utf-8", 'strict')
stringEncodedUtf16 = string1.encode("utf-16", 'strict')
stringEncodedUtf32 = string1.encode("utf-32", 'strict')
# stringEncoded = base64.b64encode(stringEncodedUtf)
# stringDecoded = base64.b64decode(stringEncoded)
# print(stringEncoded)
# print(stringDecoded)
print(stringEncodedBig5)
print(stringEncodedUtf8)
print(stringEncodedUtf16)
print(stringEncodedUtf32)

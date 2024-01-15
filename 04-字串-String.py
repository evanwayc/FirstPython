# 字符轉義 \  (溢出字元)

msg1 = 'abcdefght'
msg2 = "abcdefght"

msg3 = 'abc"def"ght'
msg4 = "abc'def'ght"

msg5 = 'abc\'def\'ght'
msg6 = "abc\"def\"ght"

print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(msg6)

print("==================")

desc = r"This is \hello\ "    # r = raw, 不會轉義字元
print(desc)

print("==================")

# '''xxxxx''' 多行字串
str = """\
第一行
第二行
第三行\
"""
print(str)

print("==================")
# 字符串中的變量
str_a = "Evan"
str_all = f"Hello, {str_a}!"
print(str_all)
print(len(str_a))
print(str_a[0])
print(str_a[-1])
print(str_a[0:3:2])

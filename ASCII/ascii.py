print(chr(66))
print(ord('A'))

a = hex(66)
b = hex(ord("A"))
print(a, b)



for i in range(0, 127):
    print(chr(i), end='')
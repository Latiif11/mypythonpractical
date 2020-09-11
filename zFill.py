# {:b} = bnary
print('{:b}'.format(10).zfill(15)) # numbet =10 , totall palece = 15

x = 10

print('{:b}'.format(x).zfill(15))

# {:+x} = hexadeecimali
print('{:x}'.format(x).zfill(15))

#{:o}= octal
print('{:o}'.format(x).zfill(15))

#{:d} = decimal, ox11 =17
print('{:d}'.format(x).zfill(0x11))
#{:d} = decimal 0b11 = 3
print('{:d}'.format(x).zfill(0b11))
#{:d} = decimal, 0o11 = 9
print('{:d}'.format(x).zfill(0o11))


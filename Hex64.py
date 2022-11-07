#import

from base64 import b64encode, b64decode

import os

# Convert hex to base64

os.system('clear')

# hex -> base64

Hex = input('\nMasukkan Hex : ')

os.system('clear')

print("Convert Hex -> Base64")

b64 = b64encode(bytes.fromhex(Hex)).decode()

print('BASE64 :', b64)

print("")

# base64 -> hex

print("Convert Base64 -> Hex")

B64 = b64decode(b64.encode()).hex()

print('HEX    :', B64)

assert Hex == B64

print("")

print("Create By Mozz")


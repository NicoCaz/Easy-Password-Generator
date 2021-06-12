import hashlib
import sys


palabra=sys.argv[1]+sys.argv[2]
parte_alta= hashlib.shake_128(palabra.encode())
union='@A'

final=parte_alta.hexdigest(8)+union
print()
print(final)
print()
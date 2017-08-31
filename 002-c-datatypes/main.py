from ctypes import *

cint1 = c_int()
print("cint1:", cint1)
print("cint1.value:", cint1.value)
print()

cint2 = c_int(8)
print("cint2:", cint2)
print("cint2.value:", cint2.value)
print()

ccharp = c_char_p(b"Henlo")
print("ccharp:", ccharp)
print("ccharp.value:", ccharp.value)
print()

cushort = c_ushort(-2)
print("cushort:", cushort)
print("cushort.value:", cushort.value)
print()
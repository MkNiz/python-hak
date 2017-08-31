from ctypes import *

cruntime = cdll.msvcrt

msg = b"Hi friend\n"
cruntime.printf(b"Test: %s", msg)
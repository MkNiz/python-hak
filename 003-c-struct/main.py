from ctypes import *

crt = cdll.msvcrt

# The structure is represented as a class that inherits the Structure class from ctypes and has a _fields_ array
# with the structure's members/types
class FELLA(Structure):
    _fields_ = [
        ("name", c_char_p),
        ("cheekiness", c_int),
    ]

# You can access these fields as if they were ordinary instance variables
def print_fella(fella):
    crt.printf(b"There's a fella named %s who's got %i cheekiness\n", fella.name, fella.cheekiness)
    
buddy = FELLA(b"Reginald", 45)
print_fella(buddy)

chum = FELLA(b"Lady Crumberly", 999)
print_fella(chum)
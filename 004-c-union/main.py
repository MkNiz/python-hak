from ctypes import *

class NUM_OF_LEGS(Union):
    _fields_ = [
        ("legs_int", c_int),
        ("legs_float", c_float),
        ("legs_long", c_long),
        ("legs_ll", c_longlong)
    ]

def leg_counter(l_union):
    print("Number of legs(int): {0}".format(l_union.legs_int))
    print("Number of legs(float): {0}".format(l_union.legs_float))
    print("Number of legs(long): {0}".format(l_union.legs_long))
    print("Number of legs(long long): {0}\n".format(l_union.legs_ll))
    
dog_legs = NUM_OF_LEGS(4)
leg_counter(dog_legs)

johns_legs = NUM_OF_LEGS(7)
leg_counter(johns_legs)

cosmic_horrors_legs = NUM_OF_LEGS(70752469325)
leg_counter(cosmic_horrors_legs)



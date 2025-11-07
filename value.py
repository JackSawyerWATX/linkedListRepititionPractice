import sys

myVal = 2025

print(f"Variable is {myVal}.")
print(f"Variable is of {type(myVal)}.")
print(f"Variable ID is {id(myVal)}.")
print(f"Variable address is {hex(id(myVal))}.")
print(f"Variable binary value is {bin(myVal)}.")
print(f"Variable binary value is {bin(myVal)[2:]}.")
print(f"Variable length is {myVal.bit_length()} bits.")
print(f"Variable size is {sys.getsizeof(myVal)} bytes.")
print(f"Variable address size is {sys.getsizeof(id(myVal))} bytes.")

# Python runs on an abstraction level above specific/direct memory allocation.

# 47
# 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1  => 8 bit
#  0     0    1    0   0   1   1   1 = 47 = 100111
#  1     1    1    1   1   1   1   1 = 255 = 11111111
# Python uses Private Heap Memory 

'''
Memory management in python involves a private heap memory to containing all python objects
The allocation of heap space for python objects is done by Python memory manager/allocator.
Python also has a build-in garbage collector which recycles all the unused memory.
'''

import gc

gc.enable() # ==> Enable automatic garbage collection.
gc.collect() # ==> recycles unused object and data structures
gc.disable() # ==> Disable garbage collection.
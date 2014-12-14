import tree

# Some constants to identify each LED
L0 = 1
L1 = 2
L2 = 4
L3 = 8
L4 = 16
L5 = 32
L6 = 64
ALL = 1+2+4+8+16+32+64
NO_LEDS = 0

tree.setup() # you must always call setup() first!

# Pattern: flash each LED in turn

while 1: # repeat FOREVER.
  for i in range (0,7,1):
    tree.leds_on_and_wait(pow(2,i) + 1, 0.3)
  for j in range (7,0,-1):
    tree.leds_on_and_wait(pow(2,j) + 1, 0.3)
  for k in range (0,ALL,1):
    tree.leds_on_and_wait(k ,0.3)
  for l in range (ALL,0,-1):
    tree.leds_on_and_wait(l,0.3)

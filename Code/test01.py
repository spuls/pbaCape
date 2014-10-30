#!/usr/bin/env python

# First we import PyBBIO:
from bbio import *

p_out = GPIO1_7

def setup():
	# Set mode
	pinMode(p_out, OUTPUT)
	
	# Set initial value
	digitalWrite(p_out, LOW)

# Create a main function
def loop():
	toggle(p_out)
	delay(500)

# start the loop
run(setup, loop)
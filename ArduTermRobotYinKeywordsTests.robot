*** Settings ***
Documentation     Yin Test cases using the keyword-driven testing approach.
...
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           ArduTermRobotTwins.py

*** Test Cases ***
Setup digital pin 13
	Setup Pin Mode		yin	13 	1	   	# input mode
	Setup Pin Status	yin	13 	0		# set yin pin
	Check Pin Status	yin	13 	0		# check yin pin

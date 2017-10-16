*** Settings ***
Documentation     Yin Yang Test cases using the keyword-driven testing approach.
...
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           ArduTermRobotTwins.py

*** Test Cases ***
Setup digital pin 02
	Setup Pin Status	01 0
	Check Pin Status	01 0

# Makefile for ArduTerm experiments
#
#
ROBOT=python -m robot

all: ArduTermRobotTwinsDemo 

tests: ArduTermRobotYinKeywordsTests ArduTermRobotYangKeywordsTests

ArduTermRobotTwinsDemo: ArduTermRobotTwinsDemo.py
	python $<

ArduTermRobotTwinsKeywordsTests: ArduTermRobotTwinsKeywordsTests.robot
	$(ROBOT) $<

ArduTermRobotYinKeywordsTests: ArduTermRobotYinKeywordsTests.robot
	$(ROBOT) $<

ArduTermRobotYangKeywordsTests: ArduTermRobotYangKeywordsTests.robot
	$(ROBOT) $<

clean:
	-@rm -rf *.csv *.log screenlog.* *.html *.pyc *.txt output.xml test1 test2

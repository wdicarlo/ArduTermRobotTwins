# Makefile for ArduTerm experiments
#
#
ROBOT=python -m robot

all: ArduTermRobotTwinsDemo 

ArduTermRobotTwinsDemo: ArduTermRobotTwinsDemo.py
	python $<

ArduTermRobotTwinsKeywordsTests: ArduTermRobotTwinsKeywordsTests.robot
	$(ROBOT) $<

clean:
	-@rm -rf *.log screenlog.* *.html *.pyc *.txt output.xml test1 test2

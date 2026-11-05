CALCULATOR
Calculator to do maths with and practice DevOps Skills

## Calculator ##
A Python 3 calculator used from the Terminal, built step by step in SCCM4910.
## What it will do ##
Add, subtract, multiply and divide two numbers; display the result.

##How to use it##
Enter first number when prompted
Enter operation (+ - * /) 
Enter second number 

## How to run it ##
Run: ./run.sh

##Development Environment##
Project uses python3 and pytest for testing
Enter SCCM4910 venv: source /opt/python-venv/sccm-4910/bin/activate

##Install Test Dependencies##
Install pytest: python3 -m pip install -r requirements-dev.txt

##Run Tests##
Run: ./check.sh

##Checking Results## 
Expect 5 passed tests, 0 failed tests
Check status using "echo $?"
Ecxpect echo check to return 0 if all test passed, 1 if a test failed, 5 means no tests were collected, any other results are liekly due to setp errors.



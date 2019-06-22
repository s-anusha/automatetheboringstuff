#! python3
# prettifiedStopwatch.py
'''
Expand the stopwatch project from this chapter so that it uses the rjust() and ljust() string methods to “prettify” the output. (These methods were covered in Chapter 6.) Instead of output such as this:

Lap #1: 3.56 (3.56)
Lap #2: 8.63 (5.07)
Lap #3: 17.68 (9.05)
Lap #4: 19.11 (1.43)
... the output will look like this:

Lap # 1:  3.56 (  3.56)
Lap # 2:  8.63 (  5.07)
Lap # 3: 17.68 (  9.05)
Lap # 4: 19.11 (  1.43)
Note that you will need string versions of the lapNum, lapTime, and totalTime integer and float variables in order to call the string methods on them.

Next, use the pyperclip module introduced in Chapter 6 to copy the text output to the clipboard so the user can quickly paste the output to a text file or email.
'''
# Usage: python prettifiedStopwatch.py

import time
# import pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1
lines = ''

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lines += 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(5), str(lapTime).rjust(6)) + '\n'
        print('Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(5), str(lapTime).rjust(6)), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy(lines)
    print('\nDone.')


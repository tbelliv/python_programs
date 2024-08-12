import pyinputplus as pyip
import sys

while True:
    response = pyip.inputYesNo(prompt='Want to know how to keep an idiot busy for hours?', blank = False, timeout=30)
    if response == 'no':
        print('Thank you, have a nice day!')
        sys.exit()
    continue

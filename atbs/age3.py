import pyinputplus as pyip
while True:
    response = pyip.inputInt(prompt='Enter a number: ', min = 4, max = 8, blank = False)
    print(f'\nYour chosen number is {response}.\nIf correct, press y.\nIf incorrect, press n.')
    confirmation = str.lower(pyip.inputStr())
    if confirmation == str('y'):
        print(f'Your number has been confirmed as {response}.')
        break
    else: 
        False
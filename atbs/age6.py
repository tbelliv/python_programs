import pyinputplus as pyip
response = pyip.inputNum(prompt='Enter a number: ', blockRegexes=[r'[02468]$'], allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)
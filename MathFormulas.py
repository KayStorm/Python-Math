#!/usr/bin/env python3
#!/usr/bin/python


userName = input('Who is this? ')
print('Hi, ' + userName)

#Selecting operator
options = {}
#     [USER OPTION] = PROGRAM RESULT
options['Exponents'] = 'exponents'
options['Addition'] = 'addition'
options['Subtraction'] = 'subtraction'
options['Multiplication'] = 'multiplication'
options['Division'] = 'division'

def selectFromDict(options, name):

  optionsList = []
  print('Select a Function:')
for optionName in options:
  index = 0
  index = index + 1
  options.extend([options[optionName]])
  print(str(index) + optionName)
inputValid = False
while not inputValid:
  inputRaw = input('Function' + ': ')
  inputNo = int(inputRaw) - 1
  if inputNo > -1 and inputNo < len(options):
     selected = options[inputNo]
     print('Selected Function: ' + selected)
     inputValid = True
     break
  else:
    print('Please select a valid number')

option = selectFromDict(options, 'option')
print('Sure! We can work on ' + selected)

#division
if selected == 5 :
  
  highNumber = float(input('What is the bigger number in the division problem? '))
  lowNumber = float(input('What is the lower number in the division problem? '))

  divisionFormula = "The answer is... "
  divisionAnswer = highNumber/lowNumber

  print(divisionFormula)
  print(divisionAnswer)

  makeSense = input('Does that answer make sense to you? Answer Y or N: ')
  print(makeSense)

  if makeSense == 'Y' or 'y':
    print('Great! We can start the next problem.')
  else:
    print('Try working it out one more time.')

else:
  print('Oops! I am still working on that!')
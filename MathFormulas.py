#!/usr/bin/env python3
#!/usr/bin/python

#division
name = input('Who is this? ')
print('Hi, ' + name)

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
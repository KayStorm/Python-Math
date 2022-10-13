#!/usr/bin/env python3
#!/usr/bin/python

import statistics

userName = input('Who is this? ')
print('Hi, ' + userName)
print("Try this calculator!")

print("I can do two sets of computations!")
print("Option a: If you give me two numbers, I can add, subtract, multiple and divide them for you.")
print("Option b: If you give me a list of numbers I can help you find mean, median, and mode")

calChoice = input("Please select which option you want to try by entering a or b: ")

if calChoice == "a" :

  x, y = [float(x) for x in input("Enter two values: ").split()]

  #addition
  print("   ~~Addition~~")

  additionMessageOne = "If you add "
  additionMessageTwo = x
  additionMessageThree = "by "
  additionMessageFour = y
  additionMessageFive = "the answer is: "
  additionAnswer = x + y

  print(additionMessageOne, additionMessageTwo, additionMessageThree, additionMessageFour, additionMessageFive, additionAnswer)

  #subtraction
  print("   ~~Subtraction~~")

  subtractionMessageOne = "If you subtract "
  subtractionMessageTwo = x
  subtractionMessageThree = "by "
  subtractionMessageFour = y
  subtractionMessageFive = "the answer is: "
  subtractionAnswer = x - y

  print(subtractionMessageOne, subtractionMessageTwo, subtractionMessageThree, subtractionMessageFour, subtractionMessageFive, subtractionAnswer)

  revsubtractionMessageOne = "If you subtract "
  revsubtractionMessageTwo = y
  revsubtractionMessageThree = "by "
  revsubtractionMessageFour = x
  revsubtractionMessageFive = "the answer is: "
  revsubtractionAnswer = y - x

  print(revsubtractionMessageOne, revsubtractionMessageTwo, revsubtractionMessageThree, revsubtractionMessageFour, revsubtractionMessageFive, revsubtractionAnswer)

  #multiply
  print("   ~~Multiplication~~")

  multiplicationMessageOne = "If you multiply "
  multiplicationMessageTwo = x
  multiplicationMessageThree = "by "
  multiplicationMessageFour = y
  multiplicationMessageFive = "the answer is: "
  multiplicationAnswer = x * y

  print(multiplicationMessageOne, multiplicationMessageTwo, multiplicationMessageThree, multiplicationMessageFour, multiplicationMessageFive, multiplicationAnswer)

  #division
  print("   ~~Division~~")

  divisionMessageOne = "If you divide "
  divisionMessageTwo = x
  divisionMessageThree = "by "
  divisionMessageFour = y
  divisionMessageFive = "the answer is: "
  divisionAnswer = x/y

  print(divisionMessageOne, divisionMessageTwo, divisionMessageThree, divisionMessageFour, divisionMessageFive, divisionAnswer)

  #reverse division
  revdivisionMessageOne = "If you divide "
  revdivisionMessageTwo = y
  revdivisionMessageThree = "by "
  revdivisionMessageFour = x
  revdivisionMessageFive = "the answer is: "
  revdivisionAnswer = y/x

  print(revdivisionMessageOne, revdivisionMessageTwo, revdivisionMessageThree, revdivisionMessageFour, revdivisionMessageFive, revdivisionAnswer)

  print("Have a great day!")

else:
  print("Enter numbers in any order with just a space between: ")
  numList = list(map(float, input().split()))
  numList.sort()
  print("   ~~Ordered List~~")
  print(*numList)

  print("   ~~Mean~~")
  print(statistics.mean(numList))

  print("   ~~Median~~")
  print(statistics.median(numList))

  print("   ~~Mode~~")
  mode = statistics.mode(numList)
  if mode == min(numList):
    print("All numbers are unique. No mode.")
  else:
    print(mode)
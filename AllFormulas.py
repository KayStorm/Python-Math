#!/usr/bin/env python3
#!/usr/bin/python

userName = input('Who is this? ')
print('Hi, ' + userName)
print("Try this calculator!")

highNumber = float(input('What is the bigger number in the problem? '))
lowNumber = float(input('What is the lower number in the problem? '))

#addition
print("   ~~Addition~~")

additionMessageOne = "If you add "
additionMessageTwo = highNumber
additionMessageThree = "by "
additionMessageFour = lowNumber
additionMessageFive = "the answer is: "
additionAnswer = highNumber + lowNumber

print(additionMessageOne, additionMessageTwo, additionMessageThree, additionMessageFour, additionMessageFive, additionAnswer)

#subtraction
print("   ~~Subtraction~~")

subtractionMessageOne = "If you subtract "
subtractionMessageTwo = highNumber
subtractionMessageThree = "by "
subtractionMessageFour = lowNumber
subtractionMessageFive = "the answer is: "
subtractionAnswer = highNumber - lowNumber

print(subtractionMessageOne, subtractionMessageTwo, subtractionMessageThree, subtractionMessageFour, subtractionMessageFive, subtractionAnswer)

revsubtractionMessageOne = "If you subtract "
revsubtractionMessageTwo = lowNumber
revsubtractionMessageThree = "by "
revsubtractionMessageFour = highNumber
revsubtractionMessageFive = "the answer is: "
revsubtractionAnswer = lowNumber - highNumber

print(revsubtractionMessageOne, revsubtractionMessageTwo, revsubtractionMessageThree, revsubtractionMessageFour, revsubtractionMessageFive, revsubtractionAnswer)

#multiply
print("   ~~Multiplication~~")

multiplicationMessageOne = "If you multiply "
multiplicationMessageTwo = highNumber
multiplicationMessageThree = "by "
multiplicationMessageFour = lowNumber
multiplicationMessageFive = "the answer is: "
multiplicationAnswer = highNumber * lowNumber

print(multiplicationMessageOne, multiplicationMessageTwo, multiplicationMessageThree, multiplicationMessageFour, multiplicationMessageFive, multiplicationAnswer)

#division
print("   ~~Division~~")

divisionMessageOne = "If you divide "
divisionMessageTwo = highNumber
divisionMessageThree = "by "
divisionMessageFour = lowNumber
divisionMessageFive = "the answer is: "
divisionAnswer = highNumber/lowNumber

print(divisionMessageOne, divisionMessageTwo, divisionMessageThree, divisionMessageFour, divisionMessageFive, divisionAnswer)

#reverse division
revdivisionMessageOne = "If you divide "
revdivisionMessageTwo = lowNumber
revdivisionMessageThree = "by "
revdivisionMessageFour = highNumber
revdivisionMessageFive = "the answer is: "
revdivisionAnswer = lowNumber/highNumber

print(revdivisionMessageOne, revdivisionMessageTwo, revdivisionMessageThree, revdivisionMessageFour, revdivisionMessageFive, revdivisionAnswer)

print("Have a great day!")